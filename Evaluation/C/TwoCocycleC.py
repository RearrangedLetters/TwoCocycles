import random

from Evaluation.C import C
from Evaluation.Auxiliary.Reformatting import extend_coordinates
from C import *
from src import Norms
from src.TwoCocycle import TwoCocycle
from src.TwoCocycleTools import *

q = [1, 0, 0, 0, 0, 0]
n = [0, 0, 0, 0, 0, 0]
r = q
mapping = [[q, q],
           [c.evaluate(q), r]]

checker = TwoCocycleTools(base)

###
# Check if the trivial condition holds, i.e. q = r in Q
###
two_cocycle = TwoCocycle(base, mapping)
print(checker.is_cocycle(C, GroupC.cayley_table, two_cocycle))


###
# Check for a_2 = b_2 = 1 if b_1 = 1 - a_1 yields two-cocycles.
# q = [a_11, a_12, a_13, a_14, a_15, a_16], similarly r described by b_ii
# a_1 = [a_11, a_12, a_13], similarly b_1
###
areTwoCocycles = True
bound = 1000
num_tests = 1000
for a_11 in random.sample(range(-bound, bound), int(np.cbrt(num_tests))):
    for a_12 in random.sample(range(-bound, bound), int(np.cbrt(num_tests))):
        for a_13 in random.sample(range(-bound, bound), int(np.cbrt(num_tests))):
            q = [a_11, a_12, a_13, 0, 0, 0]
            b_11 = 1 - a_11
            b_12 = -a_12
            b_13 = -a_13
            r = [b_11, b_12, b_13, 0, 0, 0]
            two_cocycle = TwoCocycle(base, mapping)
            if not checker.is_cocycle(C, GroupC.cayley_table, two_cocycle):
                areTwoCocycles = False
print("Random tests yielded: " + str(areTwoCocycles))


def summed_difference_var(x):
    r = [x[0], x[1]]
    q = [x[2], x[3]]
    r = extend_coordinates(r)
    q = extend_coordinates(q)
    two_cocycle = TwoCocycle(base, [[q, q],
                                    [c.evaluate(q), r]])
    return checker.summed_difference(C, cayley_table, two_cocycle, Norms.complex_euclidean)
