import copy


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


def __get_all_words_helper(Sigma, length, i, A, a):
    if i != length:
        for sigma in Sigma:
            b = copy.deepcopy(a)
            b[i] = sigma
            __get_all_words_helper(Sigma, length, i + 1, A, b)
    else:
        A.append(a)


def get_all_words(Sigma, length):
    a = [Sigma[0]] * length
    A = list()
    __get_all_words_helper(Sigma, length, 0, A, a)
    return A
