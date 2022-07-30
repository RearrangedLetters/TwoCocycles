import numpy as np

from src.TwoCocycle import TwoCocycle


def two_cocycle_from(q, R, group, base):
    mapping = [[] for _ in (range(len(group.elements)))]
    for i in range(len(R) + 1):
        for j in range(len(R) + 1):
            if i == 0 or j == 0:
                mapping[i].append(group.elements[i].apply(q))
            else:
                mapping[i].append(R[i - 1][j - 1])
    return TwoCocycle(group, base, mapping)


def two_cocycle_from_flat(x, group, base):
    dimension = ((len(group.elements) - 1) ** 2) * len(base) + len(base)
    order = len(group.elements)
    q = np.array([float(x[i]) for i in range(dimension - len(base), dimension)])
    R = [float(y) for y in x[:dimension - len(base)]]
    R = np.array(R).reshape((order - 1, order - 1, len(base)))
    return two_cocycle_from(q, R, group, base)