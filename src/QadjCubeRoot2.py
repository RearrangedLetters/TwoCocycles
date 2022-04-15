from src import TwoCocycles
from src.GroupTools import symmetric_group
import Tools


###
# The normal hull of Q(cube_root(2)) is a Galois extension of the rationals.
# Its Galois group is isomorphic to S_3. The extension thus has degree six.
# Alternatively, the splitting field of x^3 - 2 over Q has the same properties.
###

G = symmetric_group(3)


def trivial(g, h):
    return 1


TwoCocycles.print_difference(trivial, G)


# kappa_1_values = Tools.get_all_words(["1", "curt(2)"], 20)
# print(len(kappa_1_values))
