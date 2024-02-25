
"""
Napisz dwie funkcje (postaraj się wykorzystać 'list comprehension'),
z których jedna szyfruje, druga odszyfrowywuje podany
tekst przekazanym kluczem wykonując operację xor (w Pythonie operator ^) na
każdym znaku (tekst i klucz to napisy równej długości).

Przykład

tekst = 'ala' # (w ASCII:  97 108  97)
klucz = 'kot' # (w ASCII: 107 111 116)

szyfruj(tekst, klucz) = '\n\x03\x15' # \x15 to znak o kodzie 15 w systemie
                                     # szesnastkowym, czyli 21 w dziesiętnym
deszyfruj('\n\x03\x05', klucz) = 'ala'

bo:
97 ^ 107 = 10 ( = a(16), a to znak nowej linii w ASCII, '\n')
108 ^ 111= 3
97 ^ 116 = 21 (= 15(16))

Tablica ASCII:
https://en.wikipedia.org/wiki/ASCII
"""

import unittest

def szyfruj(tekst, klucz):
    pass

def deszyfruj(szyfr, klucz):
    pass


class TestXorNapisow(unittest.TestCase):

    def test_szyfrowanie(self):
        self.assertEqual(szyfruj('ala', 'kot'), '\n\x03\x15')
        self.assertEqual(szyfruj('matematyka',
                                 'qelczckwpp'),
                                '\x1c\x04\x18\x06\x17\x02\x1f\x0e\x1b\x11')
        self.assertEqual(szyfruj('hej hej',
                                 'sdkadka'),
                                 '\x1b\x01\x01A\x0c\x0e\x0b')
        self.assertEqual(szyfruj('bo Andrzej powiedzial',
                                 '930138592375934752937'),
                                 '[\\\x10p]\\GCWY\x17EVD]RQHPR[')

    def test_deszyfrowanie(self):
        self.assertEqual(deszyfruj('\n\x03\x15', 'kot'), 'ala')
        self.assertEqual(deszyfruj('\x1c\x04\x18\x06\x17\x02\x1f\x0e\x1b\x11',
                                 'qelczckwpp'),
                                'matematyka')
        self.assertEqual(deszyfruj('\x1b\x01\x01A\x0c\x0e\x0b',
                                 'sdkadka'),
                                 'hej hej')
        self.assertEqual(deszyfruj('[\\\x10p]\\GCWY\x17EVD]RQHPR[',
                                 '930138592375934752937'),
                                 'bo Andrzej powiedzial')

    def test_mix(self):
        self.assertEqual(deszyfruj(szyfruj('ala', 'kot'), 'kot'), 'ala')
        self.assertEqual(deszyfruj(szyfruj('matematyka',
                                           'qelczckwpp'), 'qelczckwpp'),
                                           'matematyka')
        self.assertEqual(deszyfruj(szyfruj('hej hej',
                                           'sdkadka'), 'sdkadka'),
                                           'hej hej')
        self.assertEqual(deszyfruj(szyfruj('bo Andrzej powiedzial',
                                            '930138592375934752937'), '930138592375934752937'),
                                            'bo Andrzej powiedzial')


if __name__ == '__main__':
    unittest.main()
