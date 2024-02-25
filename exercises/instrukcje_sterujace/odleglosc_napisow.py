
"""
Napisz funkcję, która obliczy odległość dwóch napisów od siebie. Jak ma
to wyglądać?

Załóżmy, że mamy dwa napisy długości n. Odległość jednego od drugiego liczymy
jak odległość punktów w przestrzeni R^n, tzn. jest ona pierwiastkiem kwadratowym sumy
kwadratów różnic na kolejnych współrzędnych. I tyle!

A na poważnie :)? Wcześniej opisane było jak zamienić literę na jej kod -
liczbowy odpowiednik (w jedną i w drugą stronę, funkcje ord() i chr()). To się
przyda. Musimy tylko do zrobić dla każdej litery w napisie.

Przykład:
weźmy dwa napisy trzyliterowe 'ala' i 'ola'. Ich odległość liczymy następująco:
1) zamieniamy literę na jej kod: znak 'a' ma kod 97, a znak 'o' 111
2) liczymy rożnicę: 111 - 97 = 14
3) kwadrat: 14 * 14 = 196
4) dodajemy do sumy i powtarzamy dla następnych liter
5) ostatecznie otrzymujemy sumę 196 + 0 (bo 'l' ma taki sam kod co 'l') + 0 =
196
6) ...i liczymy pierwiastek: (funkcję sqrt() można znaleźć w module math)
sqrt(196) = 14.0

Więcej o kodowaniu: www.joelonsoftware.com/articles/Unicode.html
"""

import unittest


def odleglosc_napisow(s, t):
    pass

DELTA=0.1

class TestOdlegloscNapisow(unittest.TestCase):

    def test_pojedyncze_litery(self):
        self.assertAlmostEqual(odleglosc_napisow('a', 'b'), 1.0, delta=DELTA)
        self.assertAlmostEqual(odleglosc_napisow('c', 'ć'), 164.0, delta=DELTA)
        self.assertAlmostEqual(odleglosc_napisow('a', 'z'), 25.0, delta=DELTA)
        self.assertAlmostEqual(odleglosc_napisow('ą', 'o'), 150.0, delta=DELTA)
        self.assertAlmostEqual(odleglosc_napisow('ź', 'ż'), 2.0, delta=DELTA)

    def test_jedna_litera_roznicy(self):
        self.assertAlmostEqual(odleglosc_napisow('ala',
                                                 'ola'), 14.0, delta=DELTA)
        self.assertAlmostEqual(odleglosc_napisow('buty',
                                                 'luty'), 10.0, delta=DELTA)
        self.assertAlmostEqual(odleglosc_napisow('ada',
                                                 'ida'), 8.0, delta=DELTA)
        self.assertAlmostEqual(odleglosc_napisow('rura',
                                                 'bura'), 16.0, delta=DELTA)

    def test_rozne_napisy(self):
        self.assertAlmostEqual(odleglosc_napisow('życie jest jak tramwaj',
                                                 'kluski sląskie i sosik'),
                                                 348.53, delta=DELTA)
        self.assertAlmostEqual(odleglosc_napisow('powiedział do niej tak',
                                                 '- krowa to żaden szpak'),
                                                 398.1, delta=DELTA)
        self.assertAlmostEqual(odleglosc_napisow('jestem Słowianinem',
                                                 'jestem        psem'),
                                                 340.9, delta=DELTA)
        self.assertAlmostEqual(odleglosc_napisow('tutaj już wasz program...',
                                                 'powinien być prztestowany'),
                                                 430.4, delta=DELTA)


if __name__ == '__main__':
    unittest.main()
