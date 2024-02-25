""" Napisz funkcję, która obliczy symbol Newtona, czyli "n po k".  """

import unittest


def symbol_newtona(n, k):
    pass


class TestSymbolNewtona(unittest.TestCase):

    def test_przypadki_brzegowe(self):
        self.assertEqual(symbol_newtona(0, 0), 1)
        self.assertEqual(symbol_newtona(1, 1), 1)
        self.assertEqual(symbol_newtona(5, 0), 1)
        self.assertEqual(symbol_newtona(2, 1), 2)

    def test_wieksze_liczby(self):
        self.assertEqual(symbol_newtona(10, 2), 45)
        self.assertEqual(symbol_newtona(10, 5), 252)
        self.assertEqual(symbol_newtona(31, 12), 141120525)
        self.assertEqual(symbol_newtona(52, 46), 20358520)
        self.assertEqual(symbol_newtona(100, 10), 17310309456440)


if __name__ == '__main__':
    unittest.main()
