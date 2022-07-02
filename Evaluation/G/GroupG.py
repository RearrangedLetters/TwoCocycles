###
# The Galois group G of Q_* over Q.
###
from Evaluation.QStar import *
from src.FieldAutomorphism import FieldAutomorphism
from Evaluation.C import GroupC as C
from Evaluation.D import GroupD as D

c = C.c
d = D.d
d2 = D.d2
cd = FieldAutomorphism(B, lambda x: c.apply(d.apply(x)))
cd2 = FieldAutomorphism(B, lambda x: c.apply(d2.apply(x)))

G = (id, d, d2, c, cd, cd2)

cayley_table = [[0, 0, 0, 0, 0, 0],  # todo: not correct yet
                [0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0]]
