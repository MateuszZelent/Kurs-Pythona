
"""
W analizie matematycznej definiujemy pochodną funkcji, z którą wiele
osób wczesniej czy później spotyka (np. na pierwszym roku studiów). W
algebrze w pierścieniu wielomianów lub w pierścieniu szeregów formalnych
definiuje się pochodną formalną...

Napisz funkcję, która wylicza pochodną arytmetyczną - analogon pochodnej
w teorii liczb - zdefiniowaną następująco (a' oznacza pochodną a):

>  p' = 1               jeśli p jest liczbą pierwszą (tzn. dzieli się tylko
                        przez 1 i siebie samą)
>  (ab)' = a'b + ab'    dla dowolnych liczba naturalnych a, b

Możesz zdefiniować funkcje pomocnicze. Spróbuj napisać do nich testy (najlepiej
przed stworzeniem samych funkcji - tzw. "TDD").
"""

import unittest

def pochodna_arytmetyczna(n):
    pass

class TestNumberDerivative(unittest.TestCase):

    def test_oneandzero(self):
        self.assertEqual(pochodna_arytmetyczna(0), 0)
        self.assertEqual(pochodna_arytmetyczna(1), 0)

    def test_primes(self):
        self.assertEqual(pochodna_arytmetyczna(2), 1)
        self.assertEqual(pochodna_arytmetyczna(3), 1)
        self.assertEqual(pochodna_arytmetyczna(31), 1)
        self.assertEqual(pochodna_arytmetyczna(1231), 1)
        self.assertEqual(pochodna_arytmetyczna(5393), 1)
        self.assertEqual(pochodna_arytmetyczna(419317), 1)
        self.assertEqual(pochodna_arytmetyczna(24823429), 1)

    def test_composites(self):
        self.assertEqual(pochodna_arytmetyczna(4), 4)
        self.assertEqual(pochodna_arytmetyczna(8), 12)
        self.assertEqual(pochodna_arytmetyczna(52), 56)
        self.assertEqual(pochodna_arytmetyczna(72), 156)
        self.assertEqual(pochodna_arytmetyczna(76), 80)

if __name__ == '__main__':
    unittest.main()
