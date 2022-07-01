import random

from Evaluation.QStar import *
from Evaluation.D import GroupD
from src.TwoCocycle import TwoCocycle
from src.TwoCocycleCondition import *

G = GroupD.G

q = [1, 0, 0, 0, 0, 0]
r11 = [1, 0, 0, 0, 0, 0]
r12 = [1, 0, 0, 0, 0, 0]
r21 = [1, 0, 0, 0, 0, 0]
r22 = [1, 0, 0, 0, 0, 0]
n = [0, 0, 0, 0, 0, 0]
mapping = [[q, q, n, n, n, n],
           [G[1].apply_elementwise_depr(q), r11, n, n, n, n],
           [n, n, n, n, n, n],
           [n, n, n, n, n, n],
           [n, n, n, n, n, n],
           [n, n, n, n, n, n]]

checker = TwoCocycleCondition(B)

###
# Check if the trivial condition holds, i.e. q = r in Q
###
two_cocycle = TwoCocycle(B, mapping)
print(checker.is_cocycle(G, GroupD.composition_table, two_cocycle))