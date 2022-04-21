from itertools import permutations

from src.Radical import Radical


def symmetric_group(order):
    return list(permutations([i for i in range(order)]))


def symmetric_group_functions(order):
    S = list()
    for s in symmetric_group(order):
        S.append(array_to_method(s))
    return S


def apply_permutation(p, q):
    m = [0 for _ in q]
    for i in range(len(q)):
        m[i] = q[p[i]]
    return m


# The automorphism g has to be given as its position in the array return by the method
# that generates S3.
def apply_galois_automorphism_to_base(g, r, omega):
    one = Radical(1, 1, 1)
    return [[one, r, r ** 2, omega, omega * r, omega * r ** 2],
            [one, omega * r, omega ** 2 * r ** 2, omega, omega ** 2 * r, r ** 2],
            [one, omega ** 2 * r, omega * r ** 2, omega, r, omega ** 2 * r ** 2],
            [one, r, r ** 2, omega ** 2, omega ** 2 * r, omega ** 2 * r ** 2],
            [one, omega ** 2 * r, omega * r ** 2, omega ** 2, omega * r, r ** 2],
            [one, omega * r, omega ** 2 * r ** 2, omega ** 2, r, omega * r ** 2]][g]


def apply_galois_automorphism(g, r, omega, linear_combination):
    return linear_combination.set_base(apply_galois_automorphism_to_base(g, r, omega))


def to_root_permutation(p, roots):
    return apply_permutation(p, roots)


def to_root_permutations(P, roots):
    F = list()
    for p in P:
        F.append(apply_permutation(p, roots))
    return F


def composite_permutations(p, q):
    return apply_permutation(p, q)


def composite_permutations_to_function(p, q):
    return permutation_to_method(composite_permutations(p, q))


def array_to_method(a):
    def f(x):
        return a[x]

    return f


def permutation_to_method(p):
    return array_to_method(p)


def permutations_to_method(P):
    F = list()
    for p in P:
        F.append(permutation_to_method(p))
    return F
