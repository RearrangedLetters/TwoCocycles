def isTwoCocycle(kappa, G):
    for g in G:
        for h in G:
            for k in G:
                if kappa(g, h) + kappa(g(h), k) != g(kappa(h, k)) + kappa(g, h(k)):
                    return False
    return True


def permutation_to_method(p):
    def f(x):
        return p(x)
    return f

