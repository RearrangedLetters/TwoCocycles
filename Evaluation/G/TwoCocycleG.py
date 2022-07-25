###
# Represents the Galois group of Q_* over Q.
###
from Evaluation.Auxiliary.Reformatting import two_cocycle_from_simplified
from Evaluation.G.GroupG import *
from Evaluation.QStar import *
from src import Norms
from src.TwoCocycleTools import TwoCocycleCondition

q = [1, 0, 0, 0, 0, 0]
n = [0, 0, 0, 0, 0, 0]
r11 = q
r12 = q
r13 = q
r14 = q
r15 = q

r21 = q
r22 = q
r23 = q
r24 = q
r25 = q

r31 = q
r32 = q
r33 = q
r34 = q
r35 = q

r41 = q
r42 = q
r43 = q
r44 = q
r45 = q

r51 = q
r52 = q
r53 = q
r54 = q
r55 = q

mapping = [[q, q, q, q, q, q],
           [d.apply(q), r11, r12, r13, r14, r15],
           [d2.apply(q), r21, r22, r23, r24, r25],
           [c.apply(q), r31, r32, r33, r34, r35],
           [cd.apply(q), r41, r42, r43, r44, r45],
           [cd2.apply(q), r51, r52, r53, r54, r55]]

checker = TwoCocycleCondition(B)

# two_cocycle = TwoCocycle(B, mapping)


###
# Check if the trivial condition holds
###
# print(checker.is_cocycle(D, cayley_table, two_cocycle))

###
# q is the value appearing in the first row of every 2-cocycle
# R is the matrix describing the remaining entries of the mapping
# q and each entry of R is a tuple with two elements, the real and
# complex parts which are then translated to 6-dim coordinate vectors
# the group G can work with
###
def summed_difference_simplified(q, R):
    two_cocycle = two_cocycle_from_simplified(q, R)
    return checker.summed_difference(G, cayley_table, two_cocycle, Norms.complex_euclidean)


def summed_difference_var(x):
    q, R = [x[-1], x[-2]], np.array(x[:-2]).reshape((5, 5, 2))
    return summed_difference_simplified(q, R)
