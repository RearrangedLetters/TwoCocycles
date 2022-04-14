import unittest
from TwoCocycles import *


class MyTestCase(unittest.TestCase):
    def test_do_for_all_words(self):
        for_each_word_do([0, 1], 3, print)


if __name__ == '__main__':
    unittest.main()
