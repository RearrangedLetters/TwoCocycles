from src.Radical import Radical
from src.Tools import for_each_word_do
from GroupTools import composite_permutations, apply_galois_automorphism


def eval_l(kappa, g, h, k):
    r1 = kappa(g, h)
    r2 = kappa(composite_permutations(g, h), k)
    r = r1 * r2
    return r


def eval_l_numerical(kappa, g, h, k):
    r1 = kappa(g, h)
    r2 = kappa(composite_permutations(g, h), k)
    r = r1.evaluate() * r2.evaluate()
    return r


def eval_r_g_constant(kappa, g, h, k):
    return Radical(1, 1, 1) * kappa(g, composite_permutations(h, k))


def eval_r(kappa, g, h, k, omega, r):
    return apply_galois_automorphism(g, r, omega, kappa(h, k)) * kappa(g, composite_permutations(h, k))


def eval_r_numerical(kappa, g, h, k, omega, r):
    return apply_galois_automorphism(g, r, omega, kappa(h, k)).evaluate() \
           * kappa(g, composite_permutations(h, k)).evaluate()


def eval_r_numerical_g_constant(kappa, g, h, k):
    return 1 * kappa(g, composite_permutations(h, k)).evaluate()


def is_two_cocycle(kappa, G, omega, r):
    for g in G:
        for h in G:
            for k in G:
                if eval_l(kappa, g, h, k) != eval_r(kappa, g, h, k, omega, r):
                    return False
    print(kappa)
    return True


def difference_numerical(kappa, G, omega, r):
    D = list()
    for g in G:
        for h in G:
            for k in G:
                D.append(eval_l_numerical(kappa, g, h, k) - eval_r_numerical(kappa, g, h, k, omega, r))
    return D


def print_difference(kappa, G, omega, r):
    D = list()
    for g in G:
        for h in G:
            for k in G:
                D.append(eval_l(kappa, g, h, k).evaluate() - eval_r(kappa, g, h, k, omega, r).evaluate())
    print(D)


def get_cocycles(G, E):
    for_each_word_do(E, len(G), is_two_cocycle)
