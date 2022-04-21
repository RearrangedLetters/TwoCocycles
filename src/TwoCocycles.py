from src.Radical import Radical
from src.Tools import for_each_word_do
from GroupTools import composite_permutations


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


def eval_r(kappa, g, h, k):
    return Radical(1, 1, 1) * kappa(g, composite_permutations(h, k))  # replace 1 with g(kappa(h, k))


def eval_r_numerical(kappa, g, h, k):
    return 1 * kappa(g, composite_permutations(h, k)).evaluate()  # replace 1 with g(kappa(h, k))


def is_two_cocycle(kappa, G):
    for g in G:
        for h in G:
            for k in G:
                if eval_l(kappa, g, h, k) != eval_r(kappa, g, h, k):
                    return False
    print(kappa)
    return True


def difference_numerical(kappa, G):
    D = list()
    for g in G:
        for h in G:
            for k in G:
                D.append(eval_l_numerical(kappa, g, h, k) - eval_r_numerical(kappa, g, h, k))
    return D


def print_difference(kappa, G):
    D = list()
    for g in G:
        for h in G:
            for k in G:
                D.append(eval_l(kappa, g, h, k).evaluate() - eval_r(kappa, g, h, k).evaluate())
    print(D)


def get_cocycles(G, E):
    for_each_word_do(E, len(G), is_two_cocycle)
