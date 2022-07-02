import random

from Evaluation.QStar import *
from Evaluation.D import GroupD
from Evaluation.C.GroupC import C
from src.TwoCocycle import TwoCocycle
from src.TwoCocycleCondition import *

conjugate = C[1].apply
D = GroupD.D

q = [1, 0, 0, 0, 0, 0]
n = [0, 0, 0, 0, 0, 0]
r11 = n
r12 = n
r21 = n
r22 = n
mapping = [[q, n, n],
           [conjugate(q), r11, r12],
           [conjugate(q), r21, r22]]

checker = TwoCocycleCondition(B)

###
# Check if the trivial condition holds
###
two_cocycle = TwoCocycle(B, mapping)
print(checker.is_cocycle(D, GroupD.cayley_table, two_cocycle))

