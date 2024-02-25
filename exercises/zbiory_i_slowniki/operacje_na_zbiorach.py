"""
Napisz funkcję operacje_na_zbiorach, która przyjmuje listę zbiorów oraz napis z operacjami na
zbiorach (operatorami) i zwróci wynik ich działania.

Przykład
Dla danych
[{3, 1, 4}, {6, 7, 3}, {1, 3}] '|-'

Funkcja powinna zwrócić:
{4, 6, 7}

czyli:
({3, 1, 4} | {6, 7, 3}) - {1, 3}
"""

import unittest


def operacje_na_zbiorach(zbiory, operacje):
    pass


class TestOperacjeNaZbiorach(unittest.TestCase):

    def test_pojedyncze(self):
        self.assertEqual(operacje_na_zbiorach([{1, 2}, {1}], '-'), {2})
        self.assertEqual(operacje_na_zbiorach([{'a', 'z', 'x'}, {'y', 't'}], '|'),
                                              {'a', 'x', 'y', 't', 'z'})
        self.assertEqual(operacje_na_zbiorach([{(1, 2), (1)}, {(2)}], '&'), set())
        self.assertEqual(operacje_na_zbiorach([{4, 5}, {3, 5}], '^'), {3, 4})

    def test_wielokrotne(self):
        self.assertEqual(operacje_na_zbiorach([{6, 7, 8, 9}, {6, 7},
                                               {8}, {3, 4}], '--|'),
                                              {3, 4, 9})
        self.assertEqual(operacje_na_zbiorach([{'a', 'z', 'x'},
                                               {'y', 't'},
                                               {'b', 'c', 'z'}],
                                               '|^'),
                                              {'a', 'x', 'y', 't', 'b', 'c'})
        self.assertEqual(operacje_na_zbiorach([{1, 2, 5, 9}, {2, 9},
                                               {6, 7}, {0, 6}, {1, 5}], '-|^&'),
                                               {1, 5})


if __name__ == '__main__':
    unittest.main()
