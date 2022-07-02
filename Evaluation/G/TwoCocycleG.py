###
# Represents the Galois group of Q_* over Q.
###
from Evaluation.QStar import *
from src.FieldAutomorphism import FieldAutomorphism
from Evaluation.D.GroupD import G as D
from Evaluation.C.GroupC import G as C

identity = D[0]
d = D[1]
d2 = D[2]
c = C[1]
cd = FieldAutomorphism(B, lambda x: c.apply(d.apply(x)))
cd2 = FieldAutomorphism(B, lambda x: c.apply(d2.apply(x)))

G = (identity, d, d2, c, cd, cd2)

composition_table = [[0, 1, 2, 3, 4, 5],
                     [1, 2, 0, 0, 0, 0],
                     [2, 0, 1, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0]]