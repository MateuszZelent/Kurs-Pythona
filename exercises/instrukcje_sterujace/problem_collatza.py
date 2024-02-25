
"""
Oto problem, którego żaden matematyk nie jest w stanie rozwiązać, ale każdy z
Was jest w stanie napisać program sprawdzający prawdziwość hipotezy, której on
dotyczy.

Mamy ciąg określony rekurencyjnie:
                1/2 * c(n) dla c(n) parzystego
    c(n+1) =
                3 * c(n) + 1 dla c(n) nieparzystego

Problem z nim jest taki, że nie wiadomo, czy zaczynając od jakiejkolwiek liczby
zawsze dojdziemy do 1. Twoim zadaniem jest napisanie funkcji, która pobierając
początkowy wyraz (nr 0) oblicza numer pierwszego wyrazu, który jest równy 1
(wg Wikipedii dla liczb mniejszych od 20 * 2^58 taki wyraz istnieje).
"""

import unittest

def collatz(p):
    pass


class TestProblemCollatza(unittest.TestCase):

    def test_collatz(self):
        self.assertEqual(collatz(1), 0)
        self.assertEqual(collatz(2), 1)
        self.assertEqual(collatz(8), 3)
        self.assertEqual(collatz(3), 7)
        self.assertEqual(collatz(1000), 111)
        self.assertEqual(collatz(4324), 139)
        self.assertEqual(collatz(53), 11)
        self.assertEqual(collatz(312343), 127)
        self.assertEqual(collatz(567), 61)

if __name__ == '__main__':
    unittest.main()
