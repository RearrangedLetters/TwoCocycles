###
# Represents the Galois group of Q_* over Q.
###
from Evaluation.G.GroupG import *
from Evaluation.QStar import *
from src import Norms
from src.TwoCocycle import TwoCocycle
from src.TwoCocycleTools import TwoCocycleCondition

conjugate = C[1].apply

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

mapping = [[q,            q,   q,   q,   q,   q],
           [conjugate(q), r11, r12, r13, r14, r15],
           [conjugate(q), r21, r22, r23, r24, r25],
           [conjugate(q), r31, r32, r33, r34, r35],
           [conjugate(q), r41, r42, r43, r44, r45],
           [conjugate(q), r51, r52, r53, r54, r55]]

checker = TwoCocycleCondition(B)

two_cocycle = TwoCocycle(B, mapping)

###
# Check if the trivial condition holds
###
print(checker.is_cocycle(D, cayley_table, two_cocycle))


def summed_difference_firsttwo(x_1, x_2):
    q = [x_1, x_2, 0, 0, 0, 0]
    mapping = [[q, q, q, q, q, q],
               [conjugate(q), q, q, q, q, q],
               [conjugate(q), q, q, q, q, q],
               [conjugate(q), q, q, q, q, q],
               [conjugate(q), q, q, q, q, q],
               [conjugate(q), q, q, q, q, q]]
    two_cocycle = TwoCocycle(B, mapping)
    return checker.summed_difference(G, cayley_table, two_cocycle, Norms.complex_euclidean)


