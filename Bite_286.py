from typing import Dict
from string import ascii_letters, digits


def decompress(string: str, table: Dict[str, str]) -> str:
    if string == '' or table == {}:
        return string

    chars = ascii_letters + ' ' + digits
    string = list(string)
    i = 0

    while i != len(string):
        try:
            if table.get(string[i]) and all(c in chars for c in table.get(string[i])):
                string[i] = table[string[i]]
            else:
                temp = ''.join([d for d in table.get(string[i]) if d not in chars])
                letters = ''.join([l for l in table.get(string[i]) if l in chars])
                
                string[i] = letters + decompress(temp, table) if letters == 'T' or letters == 't'\
                    else decompress(temp, table) + letters
    
        except TypeError:
            pass
        i += 1
    
    return ''.join(string)



print(decompress('Hello World!', {}))