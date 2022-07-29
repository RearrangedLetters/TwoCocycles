###
# Represents the Galois group of Q_* over Q.
###
from Evaluation.Auxiliary.Reformatting import two_cocycle_from_simplified
from Evaluation.G.G import *
from Evaluation.QStar import *
from src import Norms
from src.TwoCocycle import TwoCocycle
from src.TwoCocycleTools import TwoCocycleTools

q = [1, 0, 0, 0, 0, 0]

mapping = [[q, q, q, q, q, q],
           [d.evaluate(q), q, q, q, q, q],
           [d2.evaluate(q), q, q, q, q, q],
           [c.evaluate(q), q, q, q, q, q],
           [cd.evaluate(q), q, q, q, q, q],
           [cd2.evaluate(q), q, q, q, q, q]]

two_cocycle_G = TwoCocycle(G, Q_star.base, mapping)
checker = TwoCocycleTools(two_cocycle_G)


###
# q is the value appearing in the first row of every 2-cocycle
# R is the matrix describing the remaining entries of the mapping
# q and each entry of R is a tuple with two elements, the real and
# complex parts which are then translated to 6-dim coordinate vectors
# the group G can work with
###
def summed_difference_simplified(q, R):
    two_cocycle = two_cocycle_from_simplified(q, R)
    return TwoCocycleTools(two_cocycle).summed_difference(Norms.complex_euclidean)


def summed_difference_var(x):
    q, R = [x[-2], x[-1]], np.array(x[:-2]).reshape((5, 5, 2))
    return summed_difference_simplified(q, R)
