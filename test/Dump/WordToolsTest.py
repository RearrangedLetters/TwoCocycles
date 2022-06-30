import unittest
from src.Dump.Tools import for_each_word_do


class MyTestCase(unittest.TestCase):
    def test_do_for_all_words_1(self):
        for_each_word_do([0, 1], 2, print)

    def test_do_for_all_words_2(self):
        for_each_word_do(["a", "b", "c"], 2, print)


if __name__ == '__main__':
    unittest.main()
