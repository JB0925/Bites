from collections import Counter

def common_languages(programmers):
    """Receive a dict of keys -> names and values -> a sequence of
       of programming languages, return the common languages"""
    all = sum([item for item in programmers.values()], [])
    
    count = Counter(all)
    return [name[0] for name in count.items() if name[1] == len(programmers)]
    
    




p = dict(bob=['JS', 'PHP', 'Python', 'Perl', 'Java'],
                tim=['Python', 'Haskell', 'C++', 'JS'],
                sara=['Perl', 'C', 'Java', 'Python', 'JS'],
                paul=['C++', 'JS', 'Python'])

print(common_languages(p))