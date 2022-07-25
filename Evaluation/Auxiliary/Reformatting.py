from Evaluation.Tools import extend_coordinates, extend_each_coordinate
from Evaluation.G.GroupG import *
from src.TwoCocycle import TwoCocycle


def two_cocycle_from_simplified(q, R):
    q = extend_coordinates(q)
    R = extend_each_coordinate(R)
    mapping = [[q, q, q, q, q, q],
               [d.apply(q), R[0][0], R[0][1], R[0][2], R[0][3], R[0][4]],
               [d2.apply(q), R[1][0], R[1][1], R[1][2], R[1][3], R[1][4]],
               [c.apply(q), R[2][0], R[2][1], R[2][2], R[2][3], R[2][4]],
               [cd.apply(q), R[3][0], R[3][1], R[3][2], R[3][3], R[3][4]],
               [cd2.apply(q), R[4][0], R[4][1], R[4][2], R[4][3], R[4][4]]]
    return TwoCocycle(B, mapping)
