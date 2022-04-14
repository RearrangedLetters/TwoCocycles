def is_two_cocycle(kappa, G):
    for g in G:
        for h in G:
            for k in G:
                if kappa(g, h) + kappa(g(h), k) != g(kappa(h, k)) + kappa(g, h(k)):
                    return False
    print(kappa)
    return True


def __for_each_word_do_helper(Sigma, length, f, i, a):
    if i != length:
        for sigma in Sigma:
            a[i] = sigma
            __for_each_word_do_helper(Sigma, length, f, i + 1, a)
    else:
        f(a)


def for_each_word_do(Sigma, length, f):
    a = [Sigma[0]] * length
    f(a)
    __for_each_word_do_helper(Sigma, length, f, 0, a)


def get_single_cocycle(G, E):
    for_each_word_do(E, len(G), is_two_cocycle)


def array_to_method(a):
    def f(x):
        return a(x)
    return f


def permutation_to_method(p):
    return array_to_method(p)

