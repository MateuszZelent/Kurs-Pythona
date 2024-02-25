
"""
Napisz funkcję xor_slownikow, która przyjmuje dwa słownik i zwraca ich różnicę
symetryczną, tzn. wartości, które są pod kluczami znajdującymi się tylko w
jednym z nich. Wykorzystaj zbiory i operację różnicy symetrycznej.

Przykład
Dla słowników:
{ 1: 'a', 3: 'c', 5: 'e', 7: 'g'}
{ 1: 'ala', 2: 'basia', 3: 'celina', 4: 'daria'}

Funkcja powinna zwrócić:
{ 5: 'e', 2: 'basia', 7: 'g', 4: 'daria'}
"""

import unittest


def xor_slownikow(a, b):
    pass


class TestXorSlownikow(unittest.TestCase):
    def test_pusty_xor(self):
        self.assertEqual(xor_slownikow({1: 'a'}, {1: 'ala'}), dict())
        self.assertEqual(xor_slownikow({3: (1, 3)}, {3: (2,)}), dict())
        self.assertEqual(xor_slownikow({'Polska': 'Gniezno'},
                                       {'Polska': 'Kraków'}),
                                       dict())
        self.assertEqual(xor_slownikow({(3, -2, 5): 5},
                                       {(3, -2, 5): -2}),
                                       dict())

    def test_niepusty_xor(self):
        self.assertEqual(xor_slownikow({1: 'a', 3: 'c', 5: 'e', 7: 'g'},
                                       {1: 'ala', 2: 'basia',
                                        3: 'celina', 4: 'daria'}),
                                       {5: 'e', 2: 'basia',
                                        7: 'g', 4: 'daria'})
        self.assertEqual(xor_slownikow({(2, 4, 6): 2, (5, 10): 5, (7, 14): 7},
                                       {(3, 6, 9): 3, (4, 8): 4, (2, 4, 6): 1}),
                                       {(5, 10): 5, (7, 14): 7,
                                        (3, 6, 9): 3, (4, 8): 4})
        self.assertEqual(xor_slownikow({'Niemcy': 'Berlin',
                                        'Finlandia': 'Helsinki',
                                        'Polska': 'Warszawa'},
                                       {'Niemcy': 'Monachium',
                                        'Włochy': 'Rzym',
                                        'Dania': 'Kopenhaga'}),
                                       {'Finlandia': 'Helsinki',
                                        'Polska': 'Warszawa',
                                        'Włochy': 'Rzym',
                                        'Dania': 'Kopenhaga'}),


if __name__ == '__main__':
    unittest.main()
