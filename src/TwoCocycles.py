from src.Tools import for_each_word_do


def is_two_cocycle(kappa, G):
    for g in G:
        for h in G:
            for k in G:
                if kappa(g, h) + kappa(g(h), k) != g(kappa(h, k)) + kappa(g, h(k)):
                    return False
    print(kappa)
    return True


def get_single_cocycle(G, E):
    for_each_word_do(E, len(G), is_two_cocycle)


