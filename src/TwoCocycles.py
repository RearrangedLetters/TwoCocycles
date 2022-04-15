from src.Tools import for_each_word_do
from GroupTools import composite_permutations


def eval_l(kappa, g, h, k):
    return kappa(g, h) * kappa(composite_permutations(g, h), k)


def eval_r(kappa, g, h, k):
    return 1 * kappa(g, composite_permutations(h, k))  # replace 1 with g(kappa(h, k))


def is_two_cocycle(kappa, G):
    for g in G:
        for h in G:
            for k in G:
                if eval_l(kappa, g, h, k) != eval_r(kappa, g, h, k):
                    return False
    print(kappa)
    return True


def print_difference(kappa, G):
    for g in G:
        for h in G:
            for k in G:
                print(eval_l(kappa, g, h, k) - eval_r(kappa, g, h, k))


def get_cocycles(G, E):
    for_each_word_do(E, len(G), is_two_cocycle)
