from string import ascii_uppercase

# See tests for a more comprehensive complementary table
SIMPLE_COMPLEMENTS_STR = """#Reduced table with bases A, G, C, T
 Base	Complementary Base
 A	T
 T	A
 G	C
 C	G
"""


# Recommended helper function
def _clean_sequence(sequence, str_table):
    """
    Receives a DNA sequence and a str_table that defines valid (and
    complementary) bases
    Returns all sequences converted to upper case and remove invalid
    characters
    t!t%ttttAACCG --> TTTTTTAACCG
    """
    compliments = {}
    for row in str_table.splitlines()[2:]:
        row = row.split()
        compliments[row[0]] = row[-1]
    
    return ''.join([letter.upper() for letter in sequence\
    if letter.upper() in ascii_uppercase and letter.upper() in compliments])


def reverse(sequence, str_table=SIMPLE_COMPLEMENTS_STR):
    """
    Receives a DNA sequence and a str_table that defines valid (and
    complementary) bases
    Returns a reversed string of sequence while removing all characters
    not found in str_table characters
    e.g. t!t%ttttAACCG --> GCCAATTTTTT
    """
    sequence = _clean_sequence(sequence, str_table)
    return ''.join([s for s in sequence[::-1]])


def complement(sequence, str_table=SIMPLE_COMPLEMENTS_STR):
    """
    Receives a DNA sequence and a str_table that defines valid (and
    complementary) bases
    Returns a string containing complementary bases as defined in
    str_table while removing non input_sequence characters
    e.g. t!t%ttttAACCG --> AAAAAATTGGC
    """
    sequence = _clean_sequence(sequence, str_table)
    compliments = {}
    for row in str_table.splitlines()[2:]:
        row = row.split()
        compliments[row[0]] = row[-1]
    return ''.join([compliments.get(s) for s in sequence])


def reverse_complement(sequence, str_table=SIMPLE_COMPLEMENTS_STR):
    """
    Receives a DNA sequence and a str_table that defines valid (and
    complementary) bases
    Returns a string containing complementary bases as defined in str_table
    while removing non input_sequence characters
    e.g. t!t%ttttAACCG --> CGGTTAAAAAA
    """
    sequence = reverse(sequence, str_table)
    return complement(sequence, str_table)


#print(_clean_sequence('aCgtz  GT$aaC G--tTt%', SIMPLE_COMPLEMENTS_STR))
#print(reverse('t!t%ttttAACCG'))
#print(complement('t!t%ttttAACCG'))
print(reverse_complement('t!t%ttttAACCG'))