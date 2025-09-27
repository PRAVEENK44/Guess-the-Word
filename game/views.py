from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
from django.utils import timezone
from django.db.models import Q
import json
from datetime import date, datetime

from .models import CustomUser, GameWord, GameSession, GameGuess
from .utils import validate_username, validate_password, validate_word, generate_letter_feedback, is_word_correct

def home(request):
    if request.user.is_authenticated:
        if request.user.role == 'admin':
            return redirect('admin_dashboard')
        else:
            return redirect('game_board')
    return redirect('login')

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Invalid username or password.')
    
    return render(request, 'game/login.html')

def register_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')
        
        if not validate_username(username):
            messages.error(request, 'Username must be at least 5 letters (letters only).')
            return render(request, 'game/register.html')
        
        if not validate_password(password):
            messages.error(request, 'Password must be at least 5 characters with letters, numbers, and one of $, %, *, @.')
            return render(request, 'game/register.html')
        
        if password != confirm_password:
            messages.error(request, 'Passwords do not match.')
            return render(request, 'game/register.html')
        
        if CustomUser.objects.filter(username=username).exists():
            messages.error(request, 'Username already exists.')
            return render(request, 'game/register.html')
        
        user = CustomUser.objects.create_user(
            username=username,
            password=password,
            role='player'
        )
        
        messages.success(request, 'Account created successfully! Please log in.')
        return redirect('login')
    
    return render(request, 'game/register.html')

@login_required
def game_board(request):
    today = timezone.now().date()
    daily_sessions = GameSession.get_user_daily_sessions(request.user, today)
    can_play_today = daily_sessions.count() < 3
    
    active_session = GameSession.objects.filter(
        user=request.user,
        is_completed=False
    ).first()
    
    context = {
        'can_play_today': can_play_today,
        'daily_games_played': daily_sessions.count(),
        'active_session': active_session,
    }
    
    return render(request, 'game/game_board.html', context)

@login_required
def start_new_game(request):
    if request.method != 'POST':
        return JsonResponse({'error': 'Method not allowed'}, status=405)
    
    active_session = GameSession.objects.filter(
        user=request.user,
        is_completed=False
    ).first()
    
    if active_session:
        return JsonResponse({'error': 'You already have an active game. Please complete it first.'}, status=400)
    
    today = timezone.now().date()
    daily_sessions = GameSession.get_user_daily_sessions(request.user, today)
    if daily_sessions.count() >= 3:
        return JsonResponse({'error': 'Daily limit reached'}, status=400)
    
    word = GameWord.get_random_word()
    if not word:
        return JsonResponse({'error': 'No words available'}, status=500)
    
    session = GameSession.objects.create(
        user=request.user,
        word=word
    )
    
    return JsonResponse({
        'success': True,
        'session_id': session.id,
        'word_length': 5
    })

@login_required
@csrf_exempt
def submit_guess(request):
    if request.method != 'POST':
        return JsonResponse({'error': 'Method not allowed'}, status=405)
    
    try:
        data = json.loads(request.body)
        session_id = data.get('session_id')
        guess = data.get('guess', '').upper()
        
        if not validate_word(guess):
            return JsonResponse({'error': 'Invalid word format'}, status=400)
        
        session = get_object_or_404(GameSession, id=session_id, user=request.user)
        
        if session.is_completed:
            return JsonResponse({'error': 'Game session completed'}, status=400)
        
        if len(session.guesses) >= 5:
            return JsonResponse({'error': 'Maximum guesses reached'}, status=400)
        
        feedback = generate_letter_feedback(guess, session.word.word)
        is_correct = is_word_correct(guess, session.word.word)
        
        GameGuess.objects.create(
            session=session,
            word=guess,
            feedback=feedback,
            is_correct=is_correct
        )
        
        session.guesses.append(guess)
        session.save()
        
        if is_correct:
            session.is_completed = True
            session.is_won = True
            session.completed_at = timezone.now()
            session.save()
        elif len(session.guesses) >= 5:
            session.is_completed = True
            session.is_won = False
            session.completed_at = timezone.now()
            session.save()
        
        return JsonResponse({
            'success': True,
            'feedback': feedback,
            'is_correct': is_correct,
            'is_completed': session.is_completed,
            'is_won': session.is_won,
            'remaining_guesses': 5 - len(session.guesses),
            'correct_word': session.word.word if session.is_completed and not session.is_won else None
        })
        
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)

@login_required
def admin_dashboard(request):
    if request.user.role != 'admin':
        return redirect('game_board')
    
    selected_date = request.GET.get('date', timezone.now().date().isoformat())
    try:
        filter_date = datetime.strptime(selected_date, '%Y-%m-%d').date()
    except ValueError:
        filter_date = timezone.now().date()
    
    daily_stats = GameSession.get_daily_stats(filter_date)
    
    user_sessions = GameSession.objects.filter(created_at__date=filter_date)
    user_reports = []
    
    for user in CustomUser.objects.filter(role='player'):
        user_daily_sessions = user_sessions.filter(user=user)
        if user_daily_sessions.exists():
            correct_guesses = user_daily_sessions.filter(is_won=True).count()
            user_reports.append({
                'user': user,
                'words_tried': user_daily_sessions.count(),
                'correct_guesses': correct_guesses,
                'success_rate': (correct_guesses / user_daily_sessions.count() * 100) if user_daily_sessions.count() > 0 else 0
            })
    
    context = {
        'daily_stats': daily_stats,
        'user_reports': user_reports,
        'selected_date': filter_date.isoformat(),
    }
    
    return render(request, 'game/admin_dashboard.html', context)

@login_required
def get_session_data(request, session_id):
    session = get_object_or_404(GameSession, id=session_id, user=request.user)
    
    guesses_data = []
    for guess in session.game_guesses.all().order_by('created_at'):
        guesses_data.append({
            'word': guess.word,
            'feedback': guess.feedback,
            'is_correct': guess.is_correct
        })
    
    return JsonResponse({
        'session_id': session.id,
        'guesses': guesses_data,
        'is_completed': session.is_completed,
        'is_won': session.is_won,
        'remaining_guesses': 5 - len(session.guesses)
    })

@login_required
def get_daily_stats(request):
    today = timezone.now().date()
    daily_sessions = GameSession.get_user_daily_sessions(request.user, today)
    
    return JsonResponse({
        'success': True,
        'games_played': daily_sessions.count(),
        'daily_limit': 3,
        'can_play': daily_sessions.count() < 3
    })
