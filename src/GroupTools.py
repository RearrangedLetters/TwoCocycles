from itertools import permutations


def symmetric_group(order):
    return list(permutations([i for i in range(order)]))


def symmetric_group_functions(order):
    S = list()
    for s in symmetric_group(order):
        S.append(array_to_method(s))
    return S


def apply_permutation(p, l):
    m = [0 for _ in l]
    for i in range(len(l)):
        m[i] = l[p[i]]
    return m


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
