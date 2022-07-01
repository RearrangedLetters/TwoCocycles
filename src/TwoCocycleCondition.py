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

    def evaluate_left(self, G, composition_table, two_cocycle, g, h, k):
        first_result = two_cocycle.apply_elementwise_depr(g, h)
        second_result = two_cocycle.apply_elementwise_depr(composition_table[g][h], k)
        return self.__eval(first_result) * self.__eval(second_result)

    def evaluate_right(self, G, composition_table, two_cocycle, g, h, k):
        first_result = (G[g].apply_elementwise_depr(two_cocycle.apply_elementwise_depr(h, k)))
        second_result = two_cocycle.apply_elementwise_depr(g, composition_table[h][k])
        return self.__eval(first_result) * self.__eval(second_result)

    def is_local_cocycle(self, G, composition_table, two_cocycle, g, h, k):
        return self.__are_close(self.evaluate_left(G, composition_table, two_cocycle, g, h, k),
                                self.evaluate_right(G, composition_table, two_cocycle, g, h, k))

    def is_cocycle(self, G, composition_table, two_cocycle):
        size = len(self.base)
        for g in range(size):
            for h in range(size):
                for k in range(size):
                    if not self.is_local_cocycle(G, composition_table, two_cocycle, g, h, k):
                        return False
        return True

    def print_full_eval(self, G, composition_table, two_cocycle):
        size = len(self.base)
        for g in range(size):
            for h in range(size):
                for k in range(size):
                    left = self.evaluate_left(G, composition_table, two_cocycle, g, h, k)
                    right = self.evaluate_right(G, composition_table, two_cocycle, g, h, k)
                    print("(" + str(g) + ", " + str(h) + ", " + str(k) + ") \nl = " + str(left) + "\nr = " + str(right))
