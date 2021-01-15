from string import ascii_letters

def backwards_string(s):
    new_s = ''
    if len(s) == 1:
        return new_s + s[0]

    new_s += s[-1]
    return new_s + backwards_string(s[:-1])
    

def removeWhite(s):
    return ''.join([letter for letter in s if letter in ascii_letters])

def isPal(s):
    return ''.join([i for i in backwards_string(s)\
        if i in ascii_letters]) == removeWhite(s)
        



print(backwards_string('apple'))
print(isPal("hello"))