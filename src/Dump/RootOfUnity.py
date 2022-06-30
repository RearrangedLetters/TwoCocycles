from math import sin, cos, pi
import cmath


class RootOfUnity:
    def __init__(self, n, k):
        self.n = n
        self.k = k

    def numerical(self):
        return complex(cos((2 * self.k * cmath.pi) / self.n),
                       sin((2 * self.k * pi) / self.n))

    def __eq__(self, other):
        return self.n == other.n and self.k == other.n


class RootsOfUnity:
    def __init__(self, n):
        self.n = n

    def root(self, k):
        return RootOfUnity(self.n, k)

    def roots(self):
        R = list()
        for k in range(self.n):
            R.append(self.root(k))
        return R

    def root_numerical(self, k):
        return RootOfUnity(self.n, k).numerical()

    def roots_numerical(self):
        R = list()
        for k in range(self.n):
            R.append(self.root_numerical(k))
        return R

    def __eq__(self, other):
        return self.n == other.n


class GeneralRootOfUnity:
    def __init__(self, a, n):
        self.constant = a
        self.roots_of_unity = RootsOfUnity(n)

    def root(self, k):
        t = (self.constant, self.roots_of_unity.root(k))
        return t

    def roots(self):
        R = list()
        for k in range(self.roots_of_unity.n):
            R.append(self.root(k))
        return R

    def root_numerical(self, k):
        return pow(self.constant, 1 / self.roots_of_unity.n) * self.roots_of_unity.root_numerical(k)

    def roots_numerical(self):
        return [self.root_numerical(k) for k in range(self.roots_of_unity.n)]
