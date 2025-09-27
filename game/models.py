from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator
import random

class CustomUser(AbstractUser):
    ROLE_CHOICES = [
        ('admin', 'Admin'),
        ('player', 'Player'),
    ]
    
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='player')
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.username

class GameWord(models.Model):
    word = models.CharField(max_length=5, unique=True, validators=[
        RegexValidator(
            regex='^[A-Z]{5}$',
            message='Word must be exactly 5 uppercase letters'
        )
    ])
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.word
    
    @classmethod
    def get_random_word(cls):
        words = cls.objects.all()
        if words.exists():
            return random.choice(words)
        return None

class GameSession(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    word = models.ForeignKey(GameWord, on_delete=models.CASCADE)
    guesses = models.JSONField(default=list)
    is_completed = models.BooleanField(default=False)
    is_won = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    completed_at = models.DateTimeField(null=True, blank=True)
    
    def __str__(self):
        return f"{self.user.username} - {self.word.word} - {'Won' if self.is_won else 'Lost'}"
    
    @classmethod
    def get_user_daily_sessions(cls, user, date):
        return cls.objects.filter(
            user=user,
            created_at__date=date,
            is_completed=True
        )
    
    @classmethod
    def get_daily_stats(cls, date):
        sessions = cls.objects.filter(created_at__date=date)
        unique_users = sessions.values('user').distinct().count()
        correct_guesses = sessions.filter(is_won=True).count()
        total_games = sessions.count()
        
        return {
            'total_users': unique_users,
            'correct_guesses': correct_guesses,
            'total_games': total_games
        }

class GameGuess(models.Model):
    session = models.ForeignKey(GameSession, on_delete=models.CASCADE, related_name='game_guesses')
    word = models.CharField(max_length=5)
    feedback = models.JSONField()
    is_correct = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.session.user.username} - {self.word} - {self.created_at}"
