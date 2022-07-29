import re

from Evaluation.Auxiliary.Reformatting import two_cocycle_from_simplified
from Evaluation.Auxiliary.Solution import Solution
from Evaluation.G.G import *


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


def twococycle_from_array(x):
    q = x[25]
    R = np.array(x[:25]).reshape((5, 5, 2))
    return two_cocycle_from_simplified(q, R)


def twococycle_from_root(solution):
    return twococycle_from_array(solution.root)


def twococycle_from_optimize_result(result):
    x = list()
    for i in range(0, len(result.x) - 1, 2):
        x.append([result.x[i], result.x[i + 1]])
    return twococycle_from_array(x)