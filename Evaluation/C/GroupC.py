###
# Represents the group of automorphisms of the field extension of Q
# by a third root of unity.
###
from Evaluation.QStar import *
from src.FieldAutomorphism import FieldAutomorphism


###
# Realizes the complex conjugation on a coordinate vector respective
# to the base given above. Most importantly: conj(omega) = -omega - 1
###
def conjugate(coordinate_vector):  # todo: this method most likely has a bug
    assert len(coordinate_vector) == len(B)
    y = coordinate_vector
    x_1 = y[0] - y[3]
    x_2 = y[1] - y[4]
    x_3 = y[2] - y[5]
    x_4 = -y[3]
    x_5 = -y[4]
    x_6 = -y[5]
    return [x_1, x_2, x_3, x_4, x_5, x_6]


c = FieldAutomorphism(B, conjugate)

C = (id, c)

cayley_table = [[0, 1],
                [1, 0]]