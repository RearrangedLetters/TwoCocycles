import copy

from src.LinearCombination import LinearCombination
from src.Number import Number
from src.Radical import Radical


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
    total = len(Sigma) ** length
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


def to_int_linear_combination(w):
    L = w.split("+")
    scalars = list()
    base = list()
    for l in L:
        V = l.split("*")
        scalars.append(Number(int(V[0])))
        base.append(Radical.from_str(V[1]))
    return LinearCombination(base, scalars)
