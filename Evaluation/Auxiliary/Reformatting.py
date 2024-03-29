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


def two_cocycle_from_flat_simplified(x, group, base, positions):
    dimension = ((len(group.elements) - 1) ** 2) * len(positions) + len(positions)
    order = len(group.elements)
    q_1 = [float(x[dimension - len(positions) + i]) for i in range(len(positions))]
    q = extend_vector(q_1, len(base), positions)
    R = []
    row = list()
    i = 0
    while i <= dimension - len(positions):
        r = list()
        if i > 0 and i % ((order - 1) * len(positions)) == 0:
            R.append(row)
            row = list()
        for _ in positions:
            r.append(float(x[i]))
            i = i + 1
        row.append(extend_vector(r, len(base), positions))
    R = np.array(R).reshape((order - 1, order - 1, len(base)))
    return two_cocycle_from(q, R, group, base)


def extend_vector(short, length, positions):
    long = [0 for _ in range(length)]
    last_position = 0
    for position in positions:
        long[position] = short[last_position]
        last_position = last_position + 1
    return long


def to_pure_python(mapping):
    mapping_list = list()
    for row in mapping:
        r = list()
        for entry in row:
            r.append(list(entry))
        mapping_list.append(r)
    return mapping_list
