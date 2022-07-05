import numpy as np


def euclidean(x):
    return np.sqrt(sum(map(lambda x: x ** 2, x)))


def complex_euclidean(z):
    return np.sqrt(z.real ** 2 + z.imag ** 2)


###
# real_part is the norm of the real parts of z
# imag_part is the norm of the imaginary parts of z
###
def complex_twodim(z, norm=euclidean):
    real_part = 0
    imag_part = 0
    for x in z:
        real_part = real_part + x.real ** 2
        imag_part = imag_part + x.imag ** 2
    return [np.sqrt(real_part), np.sqrt(imag_part)]
