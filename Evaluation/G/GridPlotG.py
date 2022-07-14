import numpy as np
from matplotlib import pyplot as plt
import re


def reformat(root):
    return np.array(root).reshape(26, 2)


class Solution:
    def __init__(self, root, value):
        self.root = reformat(root)
        self.value = value


def parse_roots(file="twococycles"):
    with open(file) as f:
        lines = f.readlines()
    pattern_var1 = "(-?\\d\\.\\d{8,}e\\+?-?\\d{2})(\\s{0,}|\\])"
    pattern_var2 = "(-?\\d\\.\\d{4,})(\\s+|\\])"
    roots = list()
    root = list()
    for line in lines:
        value_check = re.match("\\d\\.\\d{10,}e\\+?-?\\d{2}|\\d\\.\\d{10,}", line)
        if value_check:
            value = float(value_check.group(0))
            roots.append(Solution(root, value))
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


# file = "twococycles_in_test"
# print(len(parse_roots(file)))
# num_empty = count_empty(file)
# print(f"#Empty lines: {num_empty}")  # should be approximately equal to the number of found roots


def gather_plot_data(solutions, threshold=1):
    R = [[[], []] for _ in range(26)]
    C = []
    max_value = 0
    for solution in solutions:
        if solution.value < threshold:
            C.append(solution.value)
            #C.append(np.power(solution.value, 1/10))
            for i, pair in enumerate(solution.root):
                R[i][0].append(pair[0])
                R[i][1].append(pair[1])
                max_value = max(solution.value, max_value)

    return R, C


def grid_plot(solutions, cmap="viridis"):
    fig, ax = plt.subplots(6, 6)
    R, C = gather_plot_data(solutions)
    m = None
    for i, r in enumerate(R):
        if i < 25:
            axi = ax[int(i / 5) + 1][i % 5 + 1]
            m = axi.scatter(r[0], r[1], s=2, c=C, cmap=cmap)
        elif i == 25:
            for j in range(6):
                ax[0][j].scatter(r[0], r[1], s=2, c=C, cmap=cmap)
                ax[j][0].scatter(r[0], r[1], s=2, c=C, cmap=cmap)
    plt.colorbar(m, ax=ax)
    #plt.savefig("gridplot.png")
    plt.show()


grid_plot(parse_roots())

