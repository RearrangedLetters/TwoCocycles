import itertools
from itertools import permutations


def symmetric_group(order):
    P = list(permutations([i for i in range(order)]))
    R = list()
    p: tuple
    for p in P:
        R.append(list(p))
    return R, get_index_function(to_int_map(R, R)), get_position_function


def to_int_map(G, H):
    Gl = (tuple(g) for g in G)
    Hl = (tuple(h) for h in H)
    return {e: i for i, e in enumerate(itertools.product(Gl, Hl))}


def get_index_function(m):
    def get_ind(g, h):
        return m[tuple(g), tuple(h)]
    return get_ind


def get_index(m, g, h):
    return m[tuple(g), tuple(h)]


def get_position_function(G):
    def get_pos(i):
        return {e: i for i, e in enumerate(G)}[i]
    return get_pos


def get_position(G):
    Gt = tuple(tuple(g) for g in G)
    return {e: i for i, e in enumerate(Gt)}


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
def apply_galois_automorphism_to_base(G, g, r, omega):
    one = 1  # Radical(1, 1, 1)
    position = get_position(G)[tuple(g)]
    return [[one, r, r ** 2, omega, omega * r, omega * r ** 2],
            [one, omega * r, omega ** 2 * r ** 2, omega, omega ** 2 * r, r ** 2],
            [one, omega ** 2 * r, omega * r ** 2, omega, r, omega ** 2 * r ** 2],
            [one, r, r ** 2, omega ** 2, omega ** 2 * r, omega ** 2 * r ** 2],
            [one, omega ** 2 * r, omega * r ** 2, omega ** 2, omega * r, r ** 2],
            [one, omega * r, omega ** 2 * r ** 2, omega ** 2, r, omega * r ** 2]][position]


def apply_galois_automorphism(G, g, r, omega, linear_combination):
    linear_combination.set_base(apply_galois_automorphism_to_base(G, g, r, omega))
    return linear_combination.evaluate()


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
