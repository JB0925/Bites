import re

words = "111"
newlines = "\n\n\nAs are newlines\n\n\n"
rand = "????{{{?}}}"
z = 'ZZzz'
c = r' \\\ '
spaces = "   Spaces are fun"
tabs = "As \t\t\t are tabs\t\t"
nums = "3335567"

def count_n_repetitions(text, n=1):
    """
    Counts how often characters are followed by themselves for
    n times.

    text: UTF-8 compliant input text
    n: How often character should be repeated, defaults to 1
    """
    count = 0
    text = re.findall(r'.', text, re.DOTALL)
    idx = 0

    while idx < len(text) - n:
        new_text = []
        num = idx

        for i in range(n):
            num += 1
            new_text.append(text[num])
        
        if len(set(new_text)) == 1:
            if text[idx] == new_text[0]:
                count += 1
        idx += 1
    
    return count
        


def count_n_reps_or_n_chars_following(text, n=1, char=""):
    """
    Counts how often characters are repeated for n times, or
    followed by char n times.

    text: UTF-8 compliant input text
    n: How often character should be repeated, defaults to 1
    char: Character which also counts if repeated n times
    """
    count = 0
    text = re.findall(r'.', text, re.DOTALL)
    idx = 0

    while idx < len(text) - n:
        new_text = []
        num = idx

        for i in range(n):
            num += 1
            new_text.append(text[num])
        
        if len(set(new_text)) == 1:
            if text[idx] == new_text[0]:
                count += 1
                
        idx += 1
    
    for i in range(len(text)-1):
        if text[i] != char:
           if list(set(text[i+1:i+1+n]))[0] == char and len(list(set(text[i+1:i+1+n]))) == 1:
               print(text[i+1:i+1+n])
               count += 1

    return count


def check_surrounding_chars(text, surrounding_chars):
    """
    Count the number of times a character is surrounded by
    characters from the surrounding_chars list.

    text: UTF-8 compliant input text
    surrounding_chars: List of characters
    """
    count = 0
    text = re.findall(r'.', text, re.DOTALL)

    for i in range(len(text)-1):
        if text[i-1] in surrounding_chars and i != 0:
            if text[i+1] in surrounding_chars:
                count += 1
    return count


f2 = "Kai is mean...aarg"
ou = "\n\n\nzz newlines\n\n"
g = "Hello^there"
print(count_n_repetitions("Ä", 1))
print(count_n_reps_or_n_chars_following("zz Don't count double!", 1, 'z'))