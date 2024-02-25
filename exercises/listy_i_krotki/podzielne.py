
"""
Korzystając z wyrażeń listowych napisz funkcję o nazwie podzielne, która przyjmuje trzy argumenty:
a, b i n i zwraca dwuelementową krotkę (k, l), gdzie l jest listą liczb
całkowitych w przedziale od a do b (wyłącznie) podzielnych przez n, a k ich
liczbą, czyli długością listy l.

Przykład

Dla danych:
1 7 2

funkcja powinna zwrócić krotkę:
(3, [2, 4, 6])
"""

import unittest

def podzielne(a, b, n):
    pass


class TestPodzielne(unittest.TestCase):

    def test_podzielne(self):
        self.assertEqual(podzielne(3, 0, 3), (0, []))
        self.assertEqual(podzielne(1, 7, 2), (3, [2, 4, 6]))
        self.assertEqual(podzielne(14, 31, 5), (4, [15, 20, 25, 30]))
        self.assertEqual(podzielne(492, 555, 23), (3, [506, 529, 552]))
        self.assertEqual(podzielne(3423, 3450, 17), (1, [3434]))
        self.assertEqual(podzielne(40000, 50000, 765),
                (13, [40545, 41310, 42075, 42840, 43605, 44370, 45135, 45900,
                      46665, 47430, 48195, 48960, 49725]))


if __name__ == '__main__':
    unittest.main()
