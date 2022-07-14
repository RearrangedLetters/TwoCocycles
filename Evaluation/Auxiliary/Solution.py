import numpy as np


class Solution:
    def __init__(self, root, value, n):
        self.root = self.__reformat(root, n)
        self.value = value

    @staticmethod
    def __reformat(root, n):
        return np.array(root).reshape(n, 2)
