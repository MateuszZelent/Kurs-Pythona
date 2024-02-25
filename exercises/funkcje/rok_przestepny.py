""" Napisz funkcję czy_przestepny, która sprawdzi, czy dany rok jest przestępny."""

import unittest


def czy_przestepny(rok):
    pass


class TestCzyPrzestepny(unittest.TestCase):

    def test_przestepne_podzielne_przez_4(self):                   
        self.assertTrue(czy_przestepny(1716))
        self.assertTrue(czy_przestepny(1960))
        self.assertTrue(czy_przestepny(1964))
        self.assertTrue(czy_przestepny(1996))
        self.assertTrue(czy_przestepny(1956))
        self.assertTrue(czy_przestepny(2004))

    def test_nieprzestepne_podzielne_przez_4(self):
        self.assertTrue(not czy_przestepny(1700))
        self.assertTrue(not czy_przestepny(1800))
        self.assertTrue(not czy_przestepny(1900))
        self.assertTrue(not czy_przestepny(2100))

    def test_przestepne_podzielne_przez_400(self):
        self.assertTrue(czy_przestepny(1600))
        self.assertTrue(czy_przestepny(2000))
        self.assertTrue(czy_przestepny(2400))


if __name__ == '__main__':
    unittest.main()
