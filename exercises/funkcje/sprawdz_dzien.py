""" Korzystając z modułu datetime napisz funkcję jaki_dzien, która pobierze datę (tzn. dzień
miesiąca, miesiąc i rok) oraz liczbę dni i zwróci napis z informacją jaki dzień będzie za n dni w
w formacie:

dzien_miesiaca.miesiac, dzien tygodnia, rok

Przykładowo, dla danych wejściowych:

1 12 2014 20

Twoja funkcja ma wypisać (7 to niedziela):

21.12, 7, 2014
"""

import unittest
import datetime

def jaki_dzien(dzien, miesiac, rok, dni):
    pass


class TestTemplate(unittest.TestCase):

    def test_ten_sam_miesiac(self):                   
        self.assertEqual(jaki_dzien(3, 10, 2002, 7), '10.10, 4, 2002')
        self.assertEqual(jaki_dzien(19, 3, 1986, 10), '29.3, 6, 1986')
        self.assertEqual(jaki_dzien(17, 9, 1991, 8), '25.9, 3, 1991')
        self.assertEqual(jaki_dzien(8, 6, 1995, 18), '26.6, 1, 1995')
        self.assertEqual(jaki_dzien(1, 1, 2100, 30), '31.1, 7, 2100')

    def test_ten_sam_rok(self):                   
        self.assertEqual(jaki_dzien(15, 4, 1984, 43), '28.5, 1, 1984')
        self.assertEqual(jaki_dzien(20, 2, 1980, 10), '1.3, 6, 1980')
        self.assertEqual(jaki_dzien(13, 6, 2000, 100), '21.9, 4, 2000')
        self.assertEqual(jaki_dzien(30, 11, 1998, 25), '25.12, 5, 1998')
        self.assertEqual(jaki_dzien(1, 1, 1930, 200), '20.7, 7, 1930')

    def test_inne(self):                   
        self.assertEqual(jaki_dzien(31, 12, 1971, 1), '1.1, 6, 1972')
        self.assertEqual(jaki_dzien(10, 6, 1954, 300), '6.4, 3, 1955')
        self.assertEqual(jaki_dzien(7, 10, 1985, 1000), '3.7, 7, 1988')
        self.assertEqual(jaki_dzien(17, 7, 1992, 2000), '7.1, 3, 1998')
        self.assertEqual(jaki_dzien(24, 9, 1910, 10000), '9.2, 3, 1938')


if __name__ == '__main__':
    unittest.main()
