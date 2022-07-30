import unittest

from src.Norms import complex_euclidean
from src.TwoCocycleTools import TwoCocycleTools
from Evaluation.G.G import *


class GTwoCocyclesTest(unittest.TestCase):
    def test_is_twococycle_01(self):
        roots = parse_roots(26, "../Evaluation/G/twococycles")
        twococycle = twococycle_from_root(roots[0])
        condition = TwoCocycleTools(twococycle)
        print(twococycle.mapping)
        print("condition yields: "
              + str(condition.summed_difference(G, cayley_table, twococycle, complex_euclidean)))


if __name__ == '__main__':
    unittest.main()
