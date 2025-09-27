import re
from typing import List, Dict, Any

def validate_username(username: str) -> bool:
    return len(username) >= 5 and re.match(r'^[a-zA-Z]+$', username) is not None

def validate_password(password: str) -> bool:
    if len(password) < 5:
        return False
    
    has_alpha = re.search(r'[a-zA-Z]', password) is not None
    has_numeric = re.search(r'\d', password) is not None
    has_special = re.search(r'[$%*@]', password) is not None
    
    return has_alpha and has_numeric and has_special

def validate_word(word: str) -> bool:
    return len(word) == 5 and re.match(r'^[A-Z]+$', word) is not None

def generate_letter_feedback(guess: str, target_word: str) -> List[Dict[str, Any]]:
    feedback = []
    target_letters = list(target_word)
    guess_letters = list(guess)
    used_target_positions = set()
    used_guess_positions = set()
    
    for i in range(len(guess_letters)):
        if guess_letters[i] == target_letters[i]:
            feedback.append({
                'letter': guess_letters[i],
                'status': 'correct',
                'position': i
            })
            used_target_positions.add(i)
            used_guess_positions.add(i)
        else:
            feedback.append(None)
    
    for i in range(len(guess_letters)):
        if used_guess_positions.intersection({i}):
            continue
            
        for j in range(len(target_letters)):
            if used_target_positions.intersection({j}):
                continue
                
            if guess_letters[i] == target_letters[j]:
                feedback[i] = {
                    'letter': guess_letters[i],
                    'status': 'present',
                    'position': i
                }
                used_target_positions.add(j)
                used_guess_positions.add(i)
                break
    
    for i in range(len(guess_letters)):
        if not used_guess_positions.intersection({i}):
            feedback[i] = {
                'letter': guess_letters[i],
                'status': 'absent',
                'position': i
            }
    
    return feedback

def is_word_correct(guess: str, target_word: str) -> bool:
    return guess == target_word
