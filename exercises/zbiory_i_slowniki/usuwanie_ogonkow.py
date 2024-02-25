
"""
Napisz funkcję usuwanie_ogonkow, która z wykorzystaniem słownika zamieni
w podanym tekście polskie znaki na ich odpowiedniki bez ogonków (itp.).
"""

import unittest

def usuwanie_ogonkow(pl_text):
    pass


class TestUsuwanieOgonkow(unittest.TestCase):
    def test_usuwanie_ogonkow(self):
        self.assertEqual(usuwanie_ogonkow('Łukasz'), 'Lukasz')
        self.assertEqual(usuwanie_ogonkow('zażółć gęślą jaźń'), 'zazolc gesla jazn')
        self.assertEqual(usuwanie_ogonkow('sączyłyście'), 'saczylyscie')
        self.assertEqual(usuwanie_ogonkow('ŃŃŃ'), 'NNN')
        self.assertEqual(usuwanie_ogonkow('ŹDŹBŁÓ'), 'ZDZBLO')
        self.assertEqual(usuwanie_ogonkow('ĆMĘ'), 'CME')
        self.assertEqual(usuwanie_ogonkow('ŁÓŻKO'), 'LOZKO')
        self.assertEqual(usuwanie_ogonkow('ZAŻÓŁĆ GĘŚLĄ JAŹŃ'), 'ZAZOLC GESLA JAZN')


if __name__ == '__main__':
    unittest.main()
