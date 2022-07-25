from Evaluation.D.GroupD import *
from Evaluation.Auxiliary.Reformatting import extend_coordinates, extend_each_coordinate
from src import Norms
from src.TwoCocycle import TwoCocycle
from src.TwoCocycleTools import *

q = [1, 0, 0, 0, 0, 0]
n = [0, 0, 0, 0, 0, 0]
r11 = n
r12 = n
r21 = n
r22 = n
mapping = [[q, n, n],
           [d.apply(q), r11, r12],
           [d2.apply(q), r21, r22]]

checker = TwoCocycleCondition(B)

###
# Check if the trivial condition holds
###
two_cocycle = TwoCocycle(B, mapping)
print(checker.is_cocycle(D, cayley_table, two_cocycle))


def summed_difference_var(x):
    q, R = [x[-1], x[-2]], x[:-2]
    R = [[[R[0], R[1]], [R[2], R[3]]],
         [[R[4], R[5]], [R[6], R[7]]]]
    R = extend_each_coordinate(R)
    q_conj = extend_coordinates([q[0], -q[1]])
    q = extend_coordinates(q)
    mapping = [[q, q, q],
               [q_conj, R[0][0], R[0][1]],
               [q_conj, R[1][0], R[1][1]]]
    two_cocycle = TwoCocycle(B, mapping)
    return checker.summed_difference(D, cayley_table, two_cocycle, Norms.complex_euclidean)
