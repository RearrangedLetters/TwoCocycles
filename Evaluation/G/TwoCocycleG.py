###
# Represents the Galois group of Q_* over Q.
###
from Evaluation.G.GroupG import *
from Evaluation.QStar import *
from Evaluation.Tools import extend_coordinates, extend_each_coordinate
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
# print(checker.is_cocycle(D, cayley_table, two_cocycle))


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


###
# q is the value appearing in the first row of every 2-cocycle
# conjugate(q) then is the value appearing in the first column
# R is the matrix describing the remaining entries of the mapping
# q and each entry of R is a tuple with two elements, the real and
# complex parts which are then translated to 6-dim coordinate vectors
# the group G can work with
###
def summed_difference_simplified_imag(q, R):
    q = extend_coordinates(q)
    R = extend_each_coordinate(R)
    mapping = [[q, q, q, q, q, q],
               [conjugate(q), R[0][0], R[0][1], R[0][2], R[0][3], R[0][4]],
               [conjugate(q), R[1][0], R[1][1], R[1][2], R[1][3], R[1][4]],
               [conjugate(q), R[2][0], R[2][1], R[2][2], R[2][3], R[2][4]],
               [conjugate(q), R[3][0], R[3][1], R[3][2], R[3][3], R[3][4]],
               [conjugate(q), R[4][0], R[4][1], R[4][2], R[4][3], R[4][4]]]
    two_cocycle = TwoCocycle(B, mapping)
    return checker.imag_summend_difference(G, cayley_table, two_cocycle, Norms.complex_twodim)


def summed_difference_simplified(q, R):
    q_conj = [[q[0], -q[1]]]
    q_conj = extend_coordinates(q_conj)
    q = extend_coordinates(q)
    R = extend_each_coordinate(R)
    mapping = [[q, q, q, q, q, q],
               [q_conj, R[0][0], R[0][1], R[0][2], R[0][3], R[0][4]],
               [q_conj, R[1][0], R[1][1], R[1][2], R[1][3], R[1][4]],
               [q_conj, R[2][0], R[2][1], R[2][2], R[2][3], R[2][4]],
               [q_conj, R[3][0], R[3][1], R[3][2], R[3][3], R[3][4]],
               [q_conj, R[4][0], R[4][1], R[4][2], R[4][3], R[4][4]]]
    two_cocycle = TwoCocycle(B, mapping)
    return checker.summed_difference(G, cayley_table, two_cocycle, Norms.complex_euclidean)


def summed_difference_simpl_const(q):
    r = [[q[0], q[1]] for _ in range(5)]
    R = [r for _ in range(5)]
    return summed_difference_simplified(q, R)


def summed_difference_var(x):
    q, R = [x[-1], x[-2]], np.array(x[:-2])
    R = R.reshape((5, 5, 2))
    return summed_difference_simplified(q, R)
