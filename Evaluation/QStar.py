###
# Q_* is the adjunction of {omega, theta} to Q, where omega is a third root of unity
# and omega is the cube root of 2. The result is a six-dimensional vector space over
# Q. This file collects same basic properties of this extension.
###
import numpy as np

from src import RootOfUnity
from src.FieldAutomorphism import FieldAutomorphism

omega = RootOfUnity.root_of_unity(3)
theta = np.cbrt(2)
B = (1, theta, theta ** 2, omega, omega * theta, omega * (theta ** 2))


id = FieldAutomorphism(B, lambda x: x)
