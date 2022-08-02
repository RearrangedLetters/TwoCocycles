import time

import numpy as np
from scipy.optimize import minimize

from Evaluation.Auxiliary.Reformatting import two_cocycle_from_flat, two_cocycle_from_flat_simplified
from src import Norms
from src.NumericalBase import NumericalBase
from src.TwoCocycleTools import TwoCocycleTools


class Solver:
    def __init__(self, group, base, zero_range=1e-3, max_error=1e-7):
        self.group = group
        self.base = base
        self.zero_range = zero_range
        self.max_error = max_error
        self.order = len(self.group.elements)
        self.dimension = ((self.order - 1) ** 2) * len(self.base) + len(self.base)

    def gather_two_cocycle_candidates(self, attempts=1, bound=1, method="BFGS", file="two_cocycles"):
        f = self.__summed_difference_flattened
        formatter = two_cocycle_from_flat
        self.__gather_candidates(f, self.dimension, formatter, attempts, bound, method, file)

    def gather_two_cocycle_candidates_simplified(self, positions, attempts=1, bound=1,
                                                 method="BFGS", file="two_cocycles_simplified"):
        file = file + "_p" + str(positions)
        f = lambda x: self.__summed_difference_flattened_simplified(x, positions)
        dimension = ((self.order - 1) ** 2) * len(positions) + len(positions)
        formatter = lambda x, group, base: two_cocycle_from_flat_simplified(x, group, base, positions)
        self.__gather_candidates(f, dimension, formatter, attempts, bound, method, file)

    def __gather_candidates(self, f, k, formatter, attempts=1, bound=1, method="BFGS", file="two_cocycles"):
        count = 0
        attempt = 1
        while attempt <= attempts:
            print(f"\nAttempt {attempt} out of {attempts}")
            start = self.__gather_starting_points(1, k, bound)[0]
            is_nonzero = self.__minimize_and_save(f, start, method, formatter, file)
            if is_nonzero:
                count = count + 1
                print(f"Found a candidate! In total {count} additional candidates were saved to {file}!")
            attempt = attempt + 1

    def __summed_difference_flattened(self, x):
        two_cocycle = two_cocycle_from_flat(x, self.group, self.base)
        tool = TwoCocycleTools(two_cocycle)
        return tool.summed_difference(norm=Norms.complex_euclidean)

    def __summed_difference_flattened_simplified(self, x, positions):
        two_cocycle = two_cocycle_from_flat_simplified(x, self.group, self.base, positions)
        tool = TwoCocycleTools(two_cocycle)
        return tool.summed_difference(norm=Norms.complex_euclidean)

    def __any_is_zero(self, x):
        for i in x:
            if abs(i) < self.zero_range:
                return True
        return False

    def __any_is_zero_eval(self, two_cocycle):
        numerical_base = NumericalBase(self.base)
        for row in two_cocycle.mapping:
            for c in row:
                if Norms.complex_euclidean(numerical_base.evaluate(c)) < self.zero_range:
                    return True
        return False

    def __gather_starting_points(self, n, k, bound=1):
        starts = list()
        for _ in range(n):
            x = np.random.rand(k)
            while self.__any_is_zero(x):
                x = np.random.rand(k)
            starts.append(np.random.rand(k))
        return np.array([x * bound for x in starts])

    def __minimize_and_save(self, f, x0, method, formatter, file):
        start = time.time()
        result = minimize(f, x0, method=method)
        duration = time.time() - start
        duration = "{:.2f}".format(duration)
        print(f"A calculation has completed, took {duration}s")

        two_cocycle = formatter(result.x, self.group, self.base)
        if self.__any_is_zero_eval(two_cocycle):
            print("Solution declined, is 0 somewhere")
            return False

        if result.fun < self.max_error:
            # factor = result.x[-len(self.base)]
            with open(file, "a") as file_object:
                file_object.write(self.__list_to_string(result.x) + "\n")
                file_object.write(str(result.fun) + "\n\n")
                file_object.close()
            return True
        else:
            print(f"Accuracy was not achieved, average error is: {result.fun}")
            return False

    @staticmethod
    def __list_to_string(L, factor=1):
        string = ""
        for l in L:
            string = string + str(l / factor) + ";"
        return string[:-1]
