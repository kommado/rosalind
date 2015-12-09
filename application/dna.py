__author__ = 'kommado'


class DnaLengthError(Exception):
    def __str__(self, *args, **kwargs):
        return "DNA string invalid length %d" % self.length

    def __init__(self, length):
        self.length = length


class InvalidDnaError(Exception):
    def __str__(self, *args, **kwargs):
        return "DNA string is invalid!. %s" % self.reason

    def __init__(self, reason):
        self.reason = reason


def count_strands(dna_string, max_length=None):

    if not dna_string:
        raise DnaLengthError(0)

    dna_length = len(dna_string)

    if max_length and dna_length > max_length:
        raise DnaLengthError(max_length)

    result = {'A': dna_string.count('A'),
              'C': dna_string.count('C'),
              'G': dna_string.count('G'),
              'T': dna_string.count('T')}

    count = 0
    for _count in result.values():
        count += _count

    if count != dna_length:
        raise InvalidDnaError("Input is not a DNA string %s" % dna_string)

    return result

def to_rna(dna_string, max_length=None):
    pass