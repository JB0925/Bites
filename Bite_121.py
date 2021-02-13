import re
from string import ascii_lowercase as lower 
from string import ascii_uppercase as upper 
from string import digits


def password_complexity(password):
    """Input: password string, calculate score according to 5 criteria in bite,
       return: score int"""
    score = 0
    repeats = 0
    special_chars = ['@','$']
    combo = lower + upper
    
    if any(p in lower for p in password)\
        and any(p in upper for p in password):
        score += 1
    
    if (any(p in special_chars for p in password)\
        and any(p in lower for p in password)) or\
        (any(p in special_chars for p in password)\
        and any(p in upper for p in password)):
        score += 1
    
    if any(p in digits for p in password)\
        and any(p in combo for p in password):
        score += 1 
    
    if len(password) >= 8:
        score += 1
    
    if all(p in special_chars for p in password):
        score += 1 
    
    for i in range(len(password)-1):
        if password[i] == password[i+1]:
            repeats += 1 
    
    if repeats == 0 and len(password) >= 8:
        score += 1 
    
    return score


print(password_complexity('123'))