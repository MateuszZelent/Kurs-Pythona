
"""
Napisz funkcję, która w podanym napisie zliczy samogłoski (aąeęioóuy).
"""

import unittest

def zlicz_samogloski(napis):
    pass


class TestSamogloski(unittest.TestCase):
    def test_brak(self):
        self.assertEqual(zlicz_samogloski('krz'), 0)
        self.assertEqual(zlicz_samogloski('bcdfghjklmnpqrstvwxz'), 0)
        self.assertEqual(zlicz_samogloski('tjkwl'), 0)
        self.assertEqual(zlicz_samogloski('hmnwhtrdng'), 0)

    def test_z_samogloskami(self):
        self.assertEqual(zlicz_samogloski('ul'), 1)
        self.assertEqual(zlicz_samogloski('ą-ę'), 2)
        self.assertEqual(zlicz_samogloski('zażółć gęślą jaźń'), 5)
        self.assertEqual(zlicz_samogloski('spartolić'), 3)
        self.assertEqual(zlicz_samogloski('ale czy na pewno?'), 6)
        self.assertEqual(zlicz_samogloski('ej, ej, ej, ej'), 4)


if __name__ == '__main__':
    unittest.main()
