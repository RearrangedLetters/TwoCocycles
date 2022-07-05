import numpy as np


def euclidean(x):
    return np.sqrt(sum(map(lambda x: x ** 2, x)))


def complex_euclidean(z):
    return np.sqrt(z.real ** 2 + z.imag ** 2)
