###
# Q_* is the adjunction of {omega, theta} to Q, where omega is a third root of unity
# and omega is the cube root of 2. The result is a six-dimensional vector space over
# Q. This file collects same basic properties of this extension.
###
import numpy as np

from src import RootOfUnity
from src.ExtensionField import ExtensionField
from src.FieldAutomorphism import FieldAutomorphism

omega = RootOfUnity.root_of_unity(3)
theta = np.cbrt(2)
base = (1, theta, theta ** 2, omega, omega * theta, omega * (theta ** 2))


###
# Realizes the complex conjugation on a coordinate vector respective
# to the base given above. Most importantly: conj(omega) = -omega - 1
###
def conjugate(coordinate_vector):
    assert len(coordinate_vector) == len(base)
    y = coordinate_vector
    x_1 = y[0] - y[3]
    x_2 = y[1] - y[4]
    x_3 = y[2] - y[5]
    x_4 = -y[3]
    x_5 = -y[4]
    x_6 = -y[5]
    return [x_1, x_2, x_3, x_4, x_5, x_6]


def d_fun(coordinate_vector):
    assert len(coordinate_vector) == len(base)
    y = coordinate_vector
    x_1 = y[0]
    x_2 = -y[4]
    x_3 = y[5] - y[2]
    x_4 = y[3]
    x_5 = y[1] - y[4]
    x_6 = -y[2]
    return [x_1, x_2, x_3, x_4, x_5, x_6]


def d2_fun(coordinate_vector):
    return d_fun(d_fun(coordinate_vector))


id = FieldAutomorphism(base, lambda x: x)
d = FieldAutomorphism(base, d_fun)
d2 = FieldAutomorphism(base, d2_fun)
c = FieldAutomorphism(base, conjugate)
cd = FieldAutomorphism(base, lambda x: c.apply(d.apply(x)))
cd2 = FieldAutomorphism(base, lambda x: c.apply(d2.apply(x)))
automorphisms = (id, d, d2, c, cd, cd2)

Q_star = ExtensionField(base, automorphisms)


def norm(x):
    prod = 0
    for g in automorphisms:
        prod = prod * g.apply(x)
    return prod
