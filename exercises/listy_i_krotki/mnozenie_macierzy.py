
"""
Napisz funkcję pomnoz_macierze(A, B), która zrobi, co jej nazwa mówi, tzn.
pomnoży macierz A przez macierz B (obie dane jako dwie listy dwuwymiarowe)i
zwróci wynik (również w formie listy).

Wskazówka: poczytaj o funkcji zip().

https://pl.wikipedia.org/wiki/Mno%C5%BCenie_macierzy
"""

import unittest

def pomnoz_macierze(A, B):
    pass


class TestPomnozMacierze(unittest.TestCase):

    def test_dwie_macierze_1x1(self):
        self.assertEqual(pomnoz_macierze([[1]], [[2]]), [[2]])
        self.assertEqual(pomnoz_macierze([[-5]], [[0]]), [[0]])
        self.assertEqual(pomnoz_macierze([[7]], [[-3]]), [[-21]])
        self.assertEqual(pomnoz_macierze([[0]], [[313]]), [[0]])
        self.assertEqual(pomnoz_macierze([[64]], [[65]]), [[4160]])
        self.assertEqual(pomnoz_macierze([[89]], [[10]]), [[890]])


    def test_dwie_macierze_2x2(self):
        self.assertEqual(pomnoz_macierze([[1, 1],
                                          [1, 1]],
                                         [[1, 0],
                                          [0, 1]]),
                         [[1, 1],
                          [1, 1]])
        self.assertEqual(pomnoz_macierze([[4, 1],
                                          [3, -5]],
                                         [[7, 1],
                                          [9, 0]]),
                         [[37, 4],
                          [-24, 3]])
        self.assertEqual(pomnoz_macierze([[-2, 11],
                                          [13, 2]],
                                         [[9, 10],
                                          [11, -12]]),
                         [[103, -152],
                          [139, 106]])

    def test_dwie_macierze_3x3(self):
        self.assertEqual(pomnoz_macierze([[1, 1, 0],
                                          [1, 1, 0],
                                          [1, 1, 0]],
                                         [[1, 0, 0],
                                          [1, 0, 0],
                                          [0, 0, 1]]),
                         [[2, 0, 0],
                          [2, 0, 0],
                          [2, 0, 0]])
        self.assertEqual(pomnoz_macierze([[1, 3, 8],
                                          [4, -2, 5],
                                          [1, -1, -4]],
                                         [[1, -4, 3],
                                          [2, -1, 4],
                                          [3, 0, 1]]),
                         [[31, -7, 23],
                          [15, -14, 9],
                          [-13, -3, -5]])
        self.assertEqual(pomnoz_macierze([[3, -1, 10],
                                          [-42, 3, 4],
                                          [3, -6, 3]],
                                         [[1, 4, -2],
                                          [33, 3, 10],
                                          [10, 17, 1]]),
                         [[70, 179, -6],
                          [97, -91, 118],
                          [-165, 45, -63]])
        self.assertEqual(pomnoz_macierze([[2, 3, 4],
                                          [5, 6, 7],
                                          [8, 9, 10]],
                                         [[-10, 9, -8],
                                          [7, -6, 5],
                                          [-4, 3, -2]]),
                         [[-15, 12, -9],
                          [-36, 30, -24],
                          [-57, 48, -39]])

    def test_dwie_macierze_roznych_wymiarow(self):
        self.assertEqual(pomnoz_macierze([[1, 0, 2],
                                          [-1, 3, 1]],
                                         [[3, 1],
                                          [2, 1],
                                          [1, 0]]),
                         [[5, 1],
                          [4, 2]])
        self.assertEqual(pomnoz_macierze([[1, -2, -3, 7],
                                          [1, 5, 2, 4]],
                                         [[3],
                                          [7],
                                          [1],
                                          [-4]]),
                         [[-42],
                          [24]])


if __name__ == '__main__':
    unittest.main()
