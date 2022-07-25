import re

import numpy as np

from Evaluation.Auxiliary.Solution import Solution
from Evaluation.C.GroupC import conjugate, C
from Evaluation.QStar import B
from Evaluation.Tools import extend_each_coordinate, extend_coordinates
from src.TwoCocycle import TwoCocycle


def parse_roots(n, file="twococycles"):
    with open(file) as f:
        lines = f.readlines()
    pattern_var1 = "(-?\\d\\.\\d+e\\+?-?\\d{2})(\\s{0,}|\\])"
    pattern_var2 = "(-?\\d\\.\\d+)(\\s+|\\])"
    roots = list()
    root = list()
    for line in lines:
        value_check = re.match("\\d\\.\\d{10,}e\\+?-?\\d{2}|\\d\\.\\d{10,}", line)
        if value_check:
            value = float(value_check.group(0))
            roots.append(Solution(root, value, n))
            root = list()
        else:
            success_check = re.match("True|False", line)
            if not success_check:
                var1_match = re.search(pattern_var1, line)
                var2_match = re.search(pattern_var2, line)
                if var1_match:
                    for match in re.finditer(pattern_var1, line):
                        root.append(float(match.group(1)))
                elif var2_match:
                    for match in re.finditer(pattern_var2, line):
                        root.append(float(match.group(1)))
    return roots


def count_empty(file="twococycles"):
    count = 0
    with open(file) as f:
        for line in f:
            if not line.strip():
                count += 1
    return count


def twococycle_from_root(solution):
    root = solution.root
    q = extend_coordinates(root[25])
    R = np.array(root[:25])
    R = R.reshape((5, 5, 2))
    R = extend_each_coordinate(R)
    conjugate = C[1].apply
    mapping = [[q, q, q, q, q, q],
               [conjugate(q), R[0][0], R[0][1], R[0][2], R[0][3], R[0][4]],
               [conjugate(q), R[1][0], R[1][1], R[1][2], R[1][3], R[1][4]],
               [conjugate(q), R[2][0], R[2][1], R[2][2], R[2][3], R[2][4]],
               [conjugate(q), R[3][0], R[3][1], R[3][2], R[3][3], R[3][4]],
               [conjugate(q), R[4][0], R[4][1], R[4][2], R[4][3], R[4][4]]]
    return TwoCocycle(B, mapping)