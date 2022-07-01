from src import RootOfUnity
from src.C import GroupC
from src.TwoCocycle import TwoCocycle
from src.TwoCocycleCondition import *

omega = RootOfUnity.root_of_unity(3)
theta = np.cbrt(2)
B = (1, omega, omega, omega ** 2, omega * theta, omega * (theta ** 2))
G = GroupC.G

q = [1, 0, 0, 0, 0, 0]
r = [1, 0, 0, 0, 0, 0]
n = [0, 0, 0, 0, 0, 0]
mapping = [[q, q, n, n, n, n],
           [G[1].apply(q), r, n, n, n, n],
           [n, n, n, n, n, n],
           [n, n, n, n, n, n],
           [n, n, n, n, n, n],
           [n, n, n, n, n, n]]

condition = TwoCocycleCondition(B)

two_cocycle = TwoCocycle(B, mapping)
# print(condition.evaluate_left(G, GroupC.composition_table, two_cocycle, 0, 0, 0))
# print(condition.evaluate_right(G, GroupC.composition_table, two_cocycle, 0, 0, 0))
print(condition.is_cocycle(G, GroupC.composition_table, two_cocycle))
# condition.print_full_eval(G, GroupC.composition_table, two_cocycle)
