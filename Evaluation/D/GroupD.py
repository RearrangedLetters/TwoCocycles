###
# Represents the group of automorphisms of the field extension of Q
# by a cube root of 2.
###
from Evaluation.QStar import *
from src.FieldAutomorphism import FieldAutomorphism


def d_fun(coordinate_vector):
    assert len(coordinate_vector) == len(B)
    y = coordinate_vector
    x_1 = y[0]
    x_2 = -y[4]
    x_3 = y[5] - y[2]
    x_4 = y[3]
    x_5 = y[1] - y[4]
    x_6 = -y[2]
    return [x_1, x_2, x_3, x_4, x_5, x_6]


def d2_fun(coordinate_vector):
    return d_fun(d_fun(coordinate_vector))


d = FieldAutomorphism(B, d_fun)
d2 = FieldAutomorphism(B, d2_fun)

D = (id, d, d2)

cayley_table = [[0, 1, 2, 0, 0, 0],
                [1, 2, 0, 0, 0, 0],
                [2, 0, 1, 0, 0, 0],
                [0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0]]
