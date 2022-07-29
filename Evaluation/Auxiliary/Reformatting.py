from src.TwoCocycle import TwoCocycle


def two_cocycle_from(q, R, group, base):
    mapping = [[] for _ in (range(len(base)))]
    for i in range(len(R) + 1):
        for j in range(len(R) + 1):
            if i == 0 or j == 0:
                mapping[i].append(group.elements[i].apply(q))
            else:
                mapping[i].append(R[i - 1][j - 1])
    return TwoCocycle(group, base, mapping)


def two_cocycle_from_simplified(q, R):
    q = extend_coordinates(q)
    R = extend_each_coordinate(R)
    mapping = [[q, q, q, q, q, q],
               [d.evaluate(q), R[0][0], R[0][1], R[0][2], R[0][3], R[0][4]],
               [d2.evaluate(q), R[1][0], R[1][1], R[1][2], R[1][3], R[1][4]],
               [c.evaluate(q), R[2][0], R[2][1], R[2][2], R[2][3], R[2][4]],
               [cd.evaluate(q), R[3][0], R[3][1], R[3][2], R[3][3], R[3][4]],
               [cd2.evaluate(q), R[4][0], R[4][1], R[4][2], R[4][3], R[4][4]]]
    return TwoCocycle(base, mapping)


def extend_coordinates(z):
    return [z[0], 0, 0, z[1], 0, 0]


def extend_each_coordinate(R):
    S = [[[0] for _ in range(5)] for _ in range(5)]
    for i, r in enumerate(R):
        for j, s in enumerate(R):
            S[i][j] = extend_coordinates(R[i][j])
    return S
