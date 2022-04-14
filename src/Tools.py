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
