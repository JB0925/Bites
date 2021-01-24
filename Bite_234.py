def capitalize_sentences(text: str) -> str:
    """Return text capitalizing the sentences. Note that sentences can end
       in dot (.), question mark (?) and exclamation mark (!)"""
    punctuation = ['.', '?','!']
    text = list(text)
    
    for i in range(len(text)-2):
        if i == 0:
            text[i] = text[i].upper()
        if text[i] in punctuation and text[i+1] == ' ':
            text[i+2] = text[i+2].upper()
    
    return ''.join(text)
        



# print(capitalize_sentences(lorem_ipsum))
