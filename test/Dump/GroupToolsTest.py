import unittest

from src.Dump.GroupTools import symmetric_group
from src.Dump.RootOfUnity import RootsOfUnity, GeneralRootOfUnity


class MyTestCase(unittest.TestCase):
    @staticmethod
    def test_symmetric_group_1():
        print(symmetric_group(3))

    @staticmethod
    def test_root_of_unity_1():
        R = RootsOfUnity(3)
        print(R.roots_numerical())

    @staticmethod
    def test_general_roots_1():
        R = GeneralRootOfUnity(2, 3)
        print(R.roots_numerical())


if __name__ == '__main__':
    unittest.main()
