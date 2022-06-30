import cmath
import unittest

from src.Dump.GroupTools import symmetric_group, to_int_map, get_index
from src.Dump.LinearCombination import LinearCombination
from src.Dump.Radical import Radical
from src.Dump.TwoCocycles import eval_r_G

S3, _, _ = symmetric_group(3)
m = to_int_map(S3, S3)
omega = Radical(cmath.e, 2j*cmath.pi, 3).evaluate()
r = Radical(2, 1, 3).evaluate()
one = Radical(1, 1, 1).evaluate()
base = [one, r, r ** 2, omega, omega * r, omega * r ** 2]


class MyTestCase(unittest.TestCase):
    def test_eval_r_01(self):
        k = [LinearCombination(base, [0, 1, 1, 0, 0, 0]) for _ in range(36)]

        def kappa(g, h):
            return k[get_index(m, g, h)]

        print("")
        print(eval_r_G(S3, kappa, r, omega))
        # print(eval_g_of_ghk(S3, kappa, r, omega))


if __name__ == '__main__':
    unittest.main()
