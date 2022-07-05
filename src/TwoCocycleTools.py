import numpy as np

from src import NumericalBase


class TwoCocycleCondition:
    delta = 1e-10

    def __init__(self, base):
        self.base = base

    def __are_close(self, x, y):
        distance = np.sqrt((x.real - y.real) ** 2 + (x.imag - y.imag) ** 2)
        return distance < self.delta

    def __eval(self, x):
        return NumericalBase.eval(self.base, x)

    def evaluate_left(self, G, cayley_table, two_cocycle, g, h, k):
        first_result = two_cocycle.apply(g, h)
        second_result = two_cocycle.apply(cayley_table[g][h], k)
        return self.__eval(first_result) * self.__eval(second_result)

    def evaluate_right(self, G, cayley_table, two_cocycle, g, h, k):
        first_result = (G[g].apply(two_cocycle.apply(h, k)))
        second_result = two_cocycle.apply(g, cayley_table[h][k])
        return self.__eval(first_result) * self.__eval(second_result)

    def is_local_cocycle(self, G, cayley_table, two_cocycle, g, h, k):
        return self.__are_close(self.evaluate_left(G, cayley_table, two_cocycle, g, h, k),
                                self.evaluate_right(G, cayley_table, two_cocycle, g, h, k))

    def is_cocycle(self, G, cayley_table, two_cocycle):
        size = len(G)
        for g in range(size):
            for h in range(size):
                for k in range(size):
                    if not self.is_local_cocycle(G, cayley_table, two_cocycle, g, h, k):
                        return False
        return True

    def print_full_eval(self, G, cayley_table, two_cocycle):
        size = len(G)
        for g in range(size):
            for h in range(size):
                for k in range(size):
                    left = self.evaluate_left(G, cayley_table, two_cocycle, g, h, k)
                    right = self.evaluate_right(G, cayley_table, two_cocycle, g, h, k)
                    print("(" + str(g) + ", " + str(h) + ", " + str(k) + ") \nl = " + str(left) + "\nr = " + str(right))

    def summed_difference(self, G, cayley_table, two_cocycle, norm):
        size = len(G)
        left_sum = 0
        right_sum = 0
        for g in range(size):
            for h in range(size):
                for k in range(size):
                    left = self.evaluate_left(G, cayley_table, two_cocycle, g, h, k)
                    right = self.evaluate_right(G, cayley_table, two_cocycle, g, h, k)
                    left_sum = left_sum + norm(left)
                    right_sum = right_sum + norm(right)
        return (left_sum - right_sum) / (size ** 3)  # todo: verify: summed_diff = 0 implies is_twococycle

    def imag_summend_difference(self, G, cayley_table, two_cocycle, norm):
        size = len(G)
        left_sum = [0, 0]
        right_sum = [0, 0]
        for g in range(size):
            for h in range(size):
                for k in range(size):
                    left = self.evaluate_left(G, cayley_table, two_cocycle, g, h, k)
                    norm_left = norm(left)
                    left_sum[0] = left_sum[0] + norm_left[0]
                    left_sum[1] = left_sum[1] + norm_left[1]
                    right = self.evaluate_right(G, cayley_table, two_cocycle, g, h, k)
                    norm_right = norm(right)
                    right_sum[0] = right_sum[0] + norm_right[0]
                    right_sum[1] = right_sum[1] + norm_right[1]
        return [(left_sum[0] - right_sum[0]) / (size ** 3), (left_sum[1] - right_sum[1]) / (size ** 3)]
