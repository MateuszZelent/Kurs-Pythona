
"""
Napisz funkcje pole_i_obwod, ktora przyjmuje jeden argument - listę
wierzchołków wielokąta (w formie krotek) - a zwraca krotkę zawierającą jego
obwód i pole.

Przykład

Dla danych:
[(0, 0), (0, 1), (1, 0)]

funkcja powinna zwrócić (w przybliżeniu - wynik będzie sprawdzany do drugiego
miejsca po przecinku):
(3.41421356, 0.5)
"""

import unittest
import math

def pole_i_obwod(wierzcholki):
    pass

def are_tuples_equal(a, b):
    DELTA = 1e-2
    result = (math.fabs(a[0] - b[0]) < DELTA and math.fabs(a[1] - b[1]) < DELTA)
    if not result:
        print ('should be: ' + str(b) + '\twas: ' + str(a))
    return result


class TestPodzielne(unittest.TestCase):

    def test_proste_przypadku(self):
        self.assertTrue(are_tuples_equal(pole_i_obwod(
                        [(0, 0), (0, 1), (1, 0)]),
                        (3.41421356, 0.5)))
        self.assertTrue(are_tuples_equal(pole_i_obwod(
                        [(0, 0), (0, 1), (1, 1), (1, 0)]),
                        (4.0, 1.0)))
        self.assertTrue(are_tuples_equal(pole_i_obwod(
                        [(0, 0), (0, 2), (1, 1), (1, 0)]),
                        (5.41421356, 1.5)))
        self.assertTrue(are_tuples_equal(pole_i_obwod(
                        [(0, 0), (0, 2), (5, 2), (5, 0)]),
                        (14.0, 10.0)))

    def test_wygibasy_wypukle(self):
        self.assertTrue(are_tuples_equal(pole_i_obwod(
                        [(-3.78, -0.77), (-5.85, -2.69), (-2.4, -4.65)]),
                        (10.909, 5.34)))
        self.assertTrue(are_tuples_equal(pole_i_obwod(
                        [(-1.43, -1.43), (-0.44, -4.55),
                         (3.31, 1.62), (-0.37, 1.39)]),
                        (17.19, 13.97)))
        self.assertTrue(are_tuples_equal(pole_i_obwod(
                        [(1.01, 4.44), (1.48, 2.19), (5.18, 1.48),
                         (4.83, 5.83), (2.6, 6.48)]),
                        (15.34, 15.3387)))
        self.assertTrue(are_tuples_equal(pole_i_obwod(
                        [(-10.99, 69.79), (-56.17, 47.07), (-69.56, -56.43),
                         (-10.37, -97.18), (71.41, -85.51), (93.72, -45.92),
                         (104.88, 14.54), (67.98, 53.3), (28.39, 77.18)]),
                        (556.1456, 22963.025)))

    def test_wygibasy_wklesle(self):
        self.assertTrue(are_tuples_equal(pole_i_obwod(
                        [(3.63, -5.87), (6.87, -4.71),
                         (4.23, -0.78), (8.92, -5.44)]),
                        (20.09, 5.436)))
        self.assertTrue(are_tuples_equal(pole_i_obwod(
                        [(-2, -8), (-1.88, -11.32), (-1.06, -9.34),
                         (2.33, -6.52), (-1.28, -8.58)]),
                        (14.9558, 3.2882)))
        self.assertTrue(are_tuples_equal(pole_i_obwod(
                        [(-60, -120), (-62.68, 23.75), (-109.6, -159.65),
                         (-10.37, -97.18), (63.32, 10.24), (93.72, -45.92),
                         (71.14, 51.42), (-24.77, -91.41), (28.39, 77.18)]),
                        (1309.29, 9801.2498)))


if __name__ == '__main__':
    unittest.main()
