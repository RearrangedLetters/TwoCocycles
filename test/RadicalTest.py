import unittest

from src.Radical import Radical


class MyTestCase(unittest.TestCase):
    def test_radical_from_string_1(self):
        s = "2^(1/3)"
        r = Radical.from_str(s)
        self.assertEqual(s, r.show())

    def test_radical_from_string_2(self):
        s = "3"
        r = Radical.from_str(s)
        self.assertEqual(s, r.show())

    def test_multiply_radicals_1(self):
        r1 = Radical(2, 1, 3)
        r2 = Radical(3, 1, 3)
        r = r1 * r2
        self.assertEqual(r, Radical(6, 1, 3))


if __name__ == '__main__':
    unittest.main()
