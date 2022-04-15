from src.Tools import for_each_word_do
from GroupTools import composite_permutations


def is_two_cocycle(kappa, G):
    for g in G:
        for h in G:
            for k in G:
                if kappa(g, h) + kappa(composite_permutations(g, h), k) !=\
                        g(kappa(h, k)) + kappa(g, composite_permutations(h, k)):
                    return False
    print(kappa)
    return True


def get_cocycles(G, E):
    for_each_word_do(E, len(G), is_two_cocycle)
