import random

from Evaluation.QStar import *
from Evaluation.D import GroupD
from Evaluation.C.GroupC import C
from src.TwoCocycle import TwoCocycle
from src.TwoCocycleCondition import *

conjugate = C[1].apply
D = GroupD.D

q = [1, 0, 0, 0, 0, 0]
r11 = q
r12 = q
r21 = q
r22 = q
n = [0, 0, 0, 0, 0, 0]
mapping = [[q, q, n, n, n, n],
           [conjugate(q), r11, r12, n, n, n],
           [conjugate(q), r21, r22, n, n, n],
           [conjugate(q), n, n, n, n, n],
           [conjugate(q), n, n, n, n, n],
           [conjugate(q), n, n, n, n, n]]

checker = TwoCocycleCondition(B)

###
# Check if the trivial condition holds
###
two_cocycle = TwoCocycle(B, mapping)
print(checker.is_cocycle(D, GroupD.cayley_table, two_cocycle))
checker.print_full_eval(D, GroupD.cayley_table, two_cocycle)