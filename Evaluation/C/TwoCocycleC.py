import random

from Evaluation.QStar import *
from Evaluation.C import GroupC
from src.TwoCocycle import TwoCocycle
from src.TwoCocycleTools import *

C = GroupC.C
conjugate = C[1].apply

q = [1, 0, 0, 0, 0, 0]
n = [0, 0, 0, 0, 0, 0]
r = q
mapping = [[q, q],
           [conjugate(q), r]]

checker = TwoCocycleCondition(B)

###
# Check if the trivial condition holds, i.e. q = r in Q
###
two_cocycle = TwoCocycle(B, mapping)
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
            two_cocycle = TwoCocycle(B, mapping)
            if not checker.is_cocycle(C, GroupC.cayley_table, two_cocycle):
                areTwoCocycles = False
print("Random tests yielded: " + str(areTwoCocycles))