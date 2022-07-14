from matplotlib import pyplot as plt


def gather_plot_data(solutions, n, threshold=1):
    R = [[[], []] for _ in range(n)]
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


def grid_plot(solutions, cmap="viridis", save=False):
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
    if save:
        plt.savefig("gridplot.png")
    plt.show()