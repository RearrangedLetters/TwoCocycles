from matplotlib import pyplot as plt

from src.NumericalBase import NumericalBase


def gather_plot_data_depr(solutions, k, threshold=1):
    R = [[[], []] for _ in range(k)]
    C = []
    max_value = 0
    for solution in solutions:
        C.append(solution.value)
        for i, pair in enumerate(solution.root):
            R[i][0].append(pair[0])
            R[i][1].append(pair[1])
            max_value = max(solution.value, max_value)
    return R, C


def grid_plot(two_cocycles):
    size = len(two_cocycles[0].mapping)
    fig, ax = plt.subplots(size, size)
    for cocycle in two_cocycles:
        mapping = cocycle.mapping
        for i, row in enumerate(mapping):
            for j, v in enumerate(row):
                value = NumericalBase(cocycle.base).evaluate(v)
                ax[i][j].scatter(value.real, value.imag)
    plt.show()