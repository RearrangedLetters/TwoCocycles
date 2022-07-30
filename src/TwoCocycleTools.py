import numpy as np

from src import Norms
from src.NumericalBase import NumericalBase


class TwoCocycleTools:
    delta = 1e-10

    def __init__(self, two_cocycle):
        self.two_cocycle = two_cocycle
        self.group = two_cocycle.group
        self.base = two_cocycle.base
        self.numerical_base = NumericalBase(self.base)

    def __are_close(self, x, y):
        distance = np.sqrt((x.real - y.real) ** 2 + (x.imag - y.imag) ** 2)
        return distance < self.delta

    def __eval(self, x):
        return self.numerical_base.evaluate(x)

    def evaluate_left(self, g, h, k):
        first_result = self.two_cocycle.evaluate(g, h)
        second_result = self.two_cocycle.evaluate(self.group.cayley_table[g][h], k)
        return self.__eval(first_result) * self.__eval(second_result)

    def evaluate_right(self, g, h, k):
        first_result = (self.group.elements[g].apply(self.two_cocycle.evaluate(h, k)))
        second_result = self.two_cocycle.evaluate(g, self.group.cayley_table[h][k])
        return self.__eval(first_result) * self.__eval(second_result)

    def is_local_cocycle(self, g, h, k):
        return self.__are_close(self.evaluate_left(g, h, k), self.evaluate_right(g, h, k))

    def is_cocycle(self):
        size = len(self.base)
        for g in range(size):
            for h in range(size):
                for k in range(size):
                    if not self.is_local_cocycle(g, h, k):
                        return False
        return True

    def print_full_eval(self):
        size = len(self.group.elements)
        for g in range(size):
            for h in range(size):
                for k in range(size):
                    left = self.evaluate_left(g, h, k)
                    right = self.evaluate_right(g, h, k)
                    print("(" + str(g) + ", " + str(h) + ", " + str(k) + ") \nl = " + str(left) + "\nr = " + str(right))

    def summed_difference(self, norm=Norms.euclidean):
        size = len(self.group.elements)
        sum = 0
        for g in range(size):
            for h in range(size):
                for k in range(size):
                    left = self.evaluate_left(g, h, k)
                    right = self.evaluate_right(g, h, k)
                    sum = sum + norm(left - right)
        return sum / (size ** 3)
