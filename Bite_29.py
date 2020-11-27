

a = ['A', 'f', '.', 'Q', 2]
b = ['.', '{', ' ^', '%', 'a']
c = [1, '=', 3, 4, 5, 'A', 'b', 'a', 'b', 'c']
d = ['=', '=', '', '/', '/', 9, ':', ';', '?', '¡']
e = list(range(1,9)) + ['}'] + list('abcde')  # noqa E230
f = [2, '.', ',', '!']



def get_index_different_char(chars):
    new_chars = [str(c) for c in chars]
    alphanumeric = ''.join(str(c) for c in new_chars if str(c).isalnum())
    non_alphanumeric = ''.join(str(c) for c in new_chars if str(c) not in alphanumeric)
    if len(alphanumeric) == 1:
        return new_chars.index(alphanumeric[0])
    else:
        return new_chars.index(non_alphanumeric[0])
    



print(get_index_different_char(f))