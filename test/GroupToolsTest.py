import unittest

from src.GroupTools import symmetric_group


class MyTestCase(unittest.TestCase):
    def test_symmetric_group_1(self):
        print(symmetric_group(3))


if __name__ == '__main__':
    unittest.main()
