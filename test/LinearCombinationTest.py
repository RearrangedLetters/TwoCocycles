import unittest

from src.LinearCombination import LinearCombination
from src.Number import Number
from src.Radical import Radical


class MyTestCase(unittest.TestCase):
    def test_something(self):
        L = LinearCombination([Number(1), Radical(2, 1, 3)], [Number(1), Number(1)])
        print(L.show())


if __name__ == '__main__':
    unittest.main()
