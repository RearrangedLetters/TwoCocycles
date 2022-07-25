from matplotlib import pyplot as plt


def gather_plot_data(solutions, k, threshold=1):
    R = [[[], []] for _ in range(k)]
    C = []
    max_value = 0
    for solution in solutions:
        if solution.value < threshold:
            C.append(solution.value)
            for i, pair in enumerate(solution.root):
                R[i][0].append(pair[0])
                R[i][1].append(pair[1])
                max_value = max(solution.value, max_value)

    return R, C


def grid_plot(solutions, size, cmap="viridis", save=False):
    k = (size - 1) ** 2 + 1
    fig, ax = plt.subplots(size, size)
    R, C = gather_plot_data(solutions, k)
    m = None
    for i, r in enumerate(R):
        if i < k - 1:
            axi = ax[int(i / (size - 1)) + 1][(i % (size - 1)) + 1]
            m = axi.scatter(r[0], r[1], s=2, c=C, cmap=cmap)
        elif i == k - 1:
            for j in range(size):
                ax[0][j].scatter(r[0], r[1], s=2, c=C, cmap=cmap)
                ax[j][0].scatter(r[0], r[1], s=2, c=C, cmap=cmap)
    if m:
        plt.colorbar(m, ax=ax)
    if save:
        plt.savefig("gridplot.png")
    plt.show()
