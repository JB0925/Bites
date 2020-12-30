from typing import List

def split_once(text: str, separators: str = None) -> List[str]:
    chars = ['\t', '\v', '\n', '\r', '\f', ' ']

    if not separators:
        if any(t in text for t in chars):
            for char in chars:
                text = '**'.join(text.split(char, maxsplit=1))
            return text.split('**')

        else:
            return text.split(' ', maxsplit=1)

    
    else:
        for sep in separators:
            text = '**'.join(text.split(sep, maxsplit=1))
        return text.split('**')
    

print(split_once(''))


