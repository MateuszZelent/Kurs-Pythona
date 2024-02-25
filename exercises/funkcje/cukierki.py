""" Łukasz skończył niedawno swoje dziesiąte programistyczne urodziny - zaczął
programować 19 września 2008 roku :-). Z tej okazji chce poczęstować swoich
kolegów cukierkami. Kupił więc m małych paczek, w każdej k cukierków i n dużych
paczek po l cukierków. W jego zespole jest p pracowników. Ile cukierków
dostanie każdy z nich?

Napisz funkcję ile_cukierkow, która przyjmuje te pięć argumentów (m, k, n, l, p)
i zwraca liczbę cukierków (całych, pozostałe wracają z Łukaszem do domu),
które dostanie każdy pracownik. Pamiętaj o możliwości zastosowaniu argumentów
domyślnych."""

import unittest
import random


def ile_cukierkow(m, k, n, l, p):
    pass


class TestIleCukierkow(unittest.TestCase):
    def test_obie_paczki(self):
        self.assertEqual(ile_cukierkow(36,35,24,109,300), 12)
        self.assertEqual(ile_cukierkow(71,19,46,128,196), 36)
        self.assertEqual(ile_cukierkow(44,39,82,155,715), 20)
        self.assertEqual(ile_cukierkow(28,18,98,72,475), 15)
        self.assertEqual(ile_cukierkow(29,18,64,58,869), 4)
        self.assertEqual(ile_cukierkow(63,38,32,138,818), 8)
        self.assertEqual(ile_cukierkow(64,29,100,136,76), 203)
        self.assertEqual(ile_cukierkow(77,20,50,120,86), 87)
        self.assertEqual(ile_cukierkow(31,37,25,147,154), 31)
        self.assertEqual(ile_cukierkow(63,17,44,145,650), 11)
        self.assertEqual(ile_cukierkow(47,39,84,134,122), 107)
        self.assertEqual(ile_cukierkow(11,25,10,173,444), 4)
        self.assertEqual(ile_cukierkow(99,6,96,166,474), 34)
        self.assertEqual(ile_cukierkow(34,45,52,133,549), 15)
        self.assertEqual(ile_cukierkow(66,44,28,103,849), 6)
        self.assertEqual(ile_cukierkow(8,22,84,176,428), 34)
        self.assertEqual(ile_cukierkow(51,34,38,149,291), 25)
        self.assertEqual(ile_cukierkow(90,29,28,160,863), 8)
        self.assertEqual(ile_cukierkow(96,18,37,71,879), 4)
        self.assertEqual(ile_cukierkow(35,9,6,79,703), 1)

    def test_tylko_wieksza(self):
        self.assertEqual(ile_cukierkow(91,31,p=178), 15)
        self.assertEqual(ile_cukierkow(93,27,p=185), 13)
        self.assertEqual(ile_cukierkow(63,2,p=165), 0)
        self.assertEqual(ile_cukierkow(22,22,p=226), 2)
        self.assertEqual(ile_cukierkow(81,33,p=196), 13)
        self.assertEqual(ile_cukierkow(28,35,p=393), 2)
        self.assertEqual(ile_cukierkow(89,30,p=85), 31)
        self.assertEqual(ile_cukierkow(39,37,p=247), 5)
        self.assertEqual(ile_cukierkow(23,28,p=131), 4)
        self.assertEqual(ile_cukierkow(29,22,p=13), 49)
        self.assertEqual(ile_cukierkow(53,23,p=5), 243)
        self.assertEqual(ile_cukierkow(38,2,p=19), 4)
        self.assertEqual(ile_cukierkow(13,48,p=462), 1)
        self.assertEqual(ile_cukierkow(71,39,p=3), 923)
        self.assertEqual(ile_cukierkow(56,34,p=295), 6)
        self.assertEqual(ile_cukierkow(25,34,p=199), 4)
        self.assertEqual(ile_cukierkow(17,33,p=156), 3)
        self.assertEqual(ile_cukierkow(93,21,p=117), 16)

    def test_tylko_mniejsza(self):
        self.assertEqual(ile_cukierkow(n=4,l=66,p=100), 2)
        self.assertEqual(ile_cukierkow(n=80,l=186,p=97), 153)
        self.assertEqual(ile_cukierkow(n=13,l=123,p=57), 28)
        self.assertEqual(ile_cukierkow(n=56,l=125,p=486), 14)
        self.assertEqual(ile_cukierkow(n=11,l=58,p=327), 1)
        self.assertEqual(ile_cukierkow(n=76,l=88,p=76), 88)
        self.assertEqual(ile_cukierkow(n=19,l=104,p=15), 131)
        self.assertEqual(ile_cukierkow(n=52,l=80,p=220), 18)
        self.assertEqual(ile_cukierkow(n=60,l=104,p=78), 80)
        self.assertEqual(ile_cukierkow(n=10,l=149,p=310), 4)
        self.assertEqual(ile_cukierkow(n=28,l=190,p=433), 12)
        self.assertEqual(ile_cukierkow(n=90,l=95,p=460), 18)
        self.assertEqual(ile_cukierkow(n=24,l=89,p=13), 164)
        self.assertEqual(ile_cukierkow(n=32,l=115,p=278), 13)
        self.assertEqual(ile_cukierkow(n=40,l=119,p=281), 16)
        self.assertEqual(ile_cukierkow(n=19,l=181,p=383), 8)
        self.assertEqual(ile_cukierkow(n=42,l=64,p=354), 7)
        self.assertEqual(ile_cukierkow(n=46,l=119,p=387), 14)
        self.assertEqual(ile_cukierkow(n=87,l=139,p=377), 32)
        self.assertEqual(ile_cukierkow(n=25,l=100,p=449), 5)


if __name__ == '__main__':
    unittest.main()
