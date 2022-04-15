import itertools

from src import TwoCocycles
from src.GroupTools import symmetric_group
import Tools
from src.Radical import Radical

###
# The normal hull of Q(cube_root(2)) is a Galois extension of the rationals.
# Its Galois group is isomorphic to S_3. The extension thus has degree six.
# Alternatively, the splitting field of x^3 - 2 over Q has the same properties.
###

S3 = symmetric_group(3)


# print(S3)


def trivial(g, h):
    return 1


def to_int_map(G, H):
    return {e: i for i, e in enumerate(itertools.product(G, H))}


# V = Tools.get_all_words(["1", "2^(1/3)"], length)
m = to_int_map(S3, S3)


def try_all_kappa_cache():
    length = 36

    V = Tools.get_all_words([Radical(1, 1, 1), Radical(2, 1, 3)], length)
    for W in V:
        def k(g, h):
            gt = tuple(g)
            ht = tuple(h)
            r = W[m[gt, ht] % length]
            return r

        TwoCocycles.difference_numerical(k, S3)


def get_and_test_kappa(w):
    def k(g, h):
        gt = tuple(g)
        ht = tuple(h)
        return w[m[gt, ht]]
    output = open("Evaluation/out/test_01", "a")
    TwoCocycles.difference_numerical(k, S3)


def try_all_kappa():
    Tools.for_each_word_do([Radical(1, 1, 1), Radical(2, 1, 3)], len(S3) ** 2, get_and_test_kappa)


try_all_kappa()

# TwoCocycles.print_difference(trivial, S3)
