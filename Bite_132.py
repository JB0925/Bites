from collections import Counter
VOWELS = list('aeiou')


def get_word_max_vowels(text):
    """Get the case insensitive word in text that has most vowels.
       Return a tuple of the matching word and the vowel count, e.g.
       ('object-oriented', 6)"""
    count = 0
    max_vowel_count = []
    text = [word.lower() for word in text.split()]
    
    for word in text:
        num_vowels = Counter([letter for letter in word\
            if letter in VOWELS])
        vowel_sum = sum(num_vowels.values())
        if vowel_sum >= count:
            count = vowel_sum
            max_vowel_count.append((word, vowel_sum))
    
    return [tup for tup in max_vowel_count if tup[1] == count]






paragraph = ("Python is an easy to learn, powerful programming language."
     "It has efficient high-level data structures and a simple "
     "but effective approach to object-oriented programming. "
     "Python’s elegant syntax and dynamic typing, together with "
     "its interpreted nature, make it an ideal language for "
     "scripting and rapid application development in many areas "
     "on most platforms.")

paragraph2 = ("The Python interpreter and the extensive standard library "
     "are freely available in source or binary form for all major "
     "platforms from the Python Web site, https://www.python.org/, "
     "and may be freely distributed. The same site also contains "
     "distributions of and pointers to many free third party Python "
     "modules, programs and tools, and additional documentation.")

paragraph3 = ("The Python interpreter is easily extended with new functions "
     "and data types implemented in C or C++ (or other languages "
     "callable from C). Python is also suitable as an extension "
     "language for customizable applications.")


print(get_word_max_vowels(paragraph3))