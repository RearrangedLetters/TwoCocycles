import unittest

from Evaluation.Auxiliary.Parser import parse_roots, twococycle_from_root
from src.Norms import complex_euclidean
from src.TwoCocycleTools import TwoCocycleCondition
from Evaluation.G.GroupG import *


class GTwoCocyclesTest(unittest.TestCase):
    def test_is_twococycle_01(self):
        roots = parse_roots(26, "../Evaluation/G/twococycles")
        twococycle = twococycle_from_root(roots[2])  # #9, #11, #21 are reasonably good #8 is better #1, #2 are great
        condition = TwoCocycleCondition(B)
        print(twococycle.mapping)
        print("condition yields: "
              + str(condition.summed_difference(G, cayley_table, twococycle, complex_euclidean)))


if __name__ == '__main__':
    unittest.main()
