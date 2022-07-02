###
# The Galois group G of Q_* over Q.
###
from Evaluation.C.GroupC import *
from Evaluation.D.GroupD import *

c = C.c
d = D.d
d2 = D.d2
cd = FieldAutomorphism(B, lambda x: c.apply(d.apply(x)))
cd2 = FieldAutomorphism(B, lambda x: c.apply(d2.apply(x)))

G = (id, d, d2, c, cd, cd2)

cayley_table = [[0, 1, 2, 3, 4, 5],
                [1, 2, 0, 5, 3, 4],
                [2, 0, 1, 4, 5, 3],
                [3, 4, 5, 0, 1, 2],
                [4, 5, 3, 2, 0, 1],
                [5, 3, 4, 1, 2, 0]]
