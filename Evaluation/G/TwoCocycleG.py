###
# Represents the Galois group of Q_* over Q.
###
from Evaluation.G.GroupG import *
from Evaluation.QStar import *
from src.TwoCocycle import TwoCocycle
from src.TwoCocycleCondition import TwoCocycleCondition

conjugate = C[1].apply

q = [1, 0, 0, 0, 0, 0]
n = [0, 0, 0, 0, 0, 0]
r11 = n
r12 = n
r13 = n
r14 = n
r15 = n

r21 = n
r22 = n
r23 = n
r24 = n
r25 = n

r31 = n
r32 = n
r33 = n
r34 = n
r35 = n

r41 = n
r42 = n
r43 = n
r44 = n
r45 = n

r51 = n
r52 = n
r53 = n
r54 = n
r55 = n

mapping = [[q,            q,   q,   q,   q,   q],
           [conjugate(q), r11, r12, r13, r14, r15],
           [conjugate(q), r21, r22, r23, r24, r25],
           [conjugate(q), r31, r32, r33, r34, r35],
           [conjugate(q), r41, r42, r43, r44, r45],
           [conjugate(q), r51, r52, r53, r54, r55]]

checker = TwoCocycleCondition(B)

###
# Check if the trivial condition holds
###
two_cocycle = TwoCocycle(B, mapping)
print(checker.is_cocycle(D, cayley_table, two_cocycle))