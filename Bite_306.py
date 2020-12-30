from Bio.Data.CodonTable import TranslationError
from Bio import Seq
from string import whitespace

def translate_cds(cds: str, translation_table: str) -> str:
    """
    :param cds: str: DNA coding sequence (CDS)
    :param translation_table: str: translation table as defined in Bio.Seq.Seq.CodonTable.ambiguous_generic_by_name
    :return: str: Protein sequence
    """
    cdss = ''.join([c for c in cds if c not in whitespace and c != '\u00A0' and c != '\u2009'])
    return Seq.translate(cdss, translation_table, cds=True)
    




print(translate_cds("ATGAA", 'Standard'))