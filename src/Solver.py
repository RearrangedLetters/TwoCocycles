from datetime import time

import numpy as np
import time
from scipy.optimize import minimize

from Evaluation.Auxiliary.Reformatting import two_cocycle_from
from src import Norms
from src.TwoCocycleTools import TwoCocycleTools


class Solver:
    def __init__(self, group, base, zero_range=1e-3, max_error=1e-6):
        self.group = group
        self.base = base
        self.zero_range = zero_range
        self.max_error = max_error
        self.order = len(self.group.elements)
        self.dimension = ((self.order - 1) ** 2) * self.order + 2

    def gather_solutions(self, attempts=1, bound=1, method="BFGS", file="two_cocycles"):
        f = self.__summed_difference_flattened
        count = 0
        attempt = 1
        while count < attempts:
            print(f"Attempt {attempt} out of {attempts}")
            start = self.__gather_starting_points(1, self.dimension, bound)[0]
            is_nonzero = self.__minimize_and_save(f, start, method, file)
            if is_nonzero:
                count = count + 1
                print(f"Found another candidate! In total {count} candidates were saved to {file}!")
            attempt = attempt + 1

    def __summed_difference_flattened(self, x):
        q = np.array([x[i] for i in range(self.dimension - self.order, self.dimension)])
        R = np.array(x[:-self.order]).reshape((self.order - 1, self.order - 1, self.order))
        two_cocycle = two_cocycle_from(q, R, self.group, self.base)
        tool = TwoCocycleTools(two_cocycle)
        return tool.summed_difference()

    def __any_is_zero(self, x):
        for i in x:
            if abs(i) < self.zero_range:
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

    def __minimize_and_save(self, f, x0, method, file):
        start = time.time()
        result = minimize(f, x0, method=method)
        duration = time.time() - start
        print(f"\nA calculation has completed, took {duration}s")
        for i in range(0, len(result.x) - 1, 2):
            if Norms.euclidean([result.x[i], result.x[i + 1]]) < self.zero_range:
                print("Solution declined, is 0 somewhere")
                return False

        if result.fun < self.max_error:
            with open(file, "a") as file_object:
                file_object.write(str(result.x))
                file_object.write("\n")
                file_object.write(str(result.success))
                file_object.write("\n")
                file_object.write(str(result.fun))
                file_object.write("\n\n")
                file_object.close()
            print("A result has been saved!")
            return True
        else:
            print("Accuracy was not achieved, average error is: " + str(result.fun))
            return False