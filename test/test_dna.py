from string import Template
import unittest

import application.dna as dna

__author__ = 'kommado'


class TestDnaMethods(unittest.TestCase):
    def test_count_strands(self):
        dna_string = "AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC"
        result = dna.count_strands(dna_string, 1000)
        self.assertEquals({'A': 20, 'C': 12, 'G': 17, 'T': 21}, result)

    def test_invalid_dna(self):

        try:
            dna.count_strands("AGCTTTTCATTCTGACTGCAACGGGCAATATGTCT", 10)
            self.fail('DNA too long')
        except dna.DnaLengthError as ex:
            self.assertEquals(ex.length, 10)

        try:
            dna.count_strands("", 10)
            self.fail('DNA zero length')
        except dna.DnaLengthError as ex:
            self.assertEquals(ex.length, 0)

        try:
            dna.count_strands("mitsos")
            self.fail('DNA mitsos string is not valid')
        except dna.InvalidDnaError as ex:
            self.assertEquals(ex.reason, 'Input is not a DNA string mitsos')

    def test_rosalind(self):
        rosalind_print = Template('$A $C $G $T')
        dna_string = open('rosalind_dna.txt').read()
        result = dna.count_strands(dna_string, 1000)
        print("Rosalind DNA: %s " % rosalind_print.substitute(result))

if __name__ == '__main__':
    unittest.main()
