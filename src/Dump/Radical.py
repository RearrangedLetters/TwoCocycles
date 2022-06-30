from src.Dump.Number import Number
import re


###
# Represents a radical. If x is the radicand which is raised to the n-the power
# and we take the r-th root. Then this class represents x^(n/r)
###
class Radical(Number):
    def __init__(self, x, n, r):
        super().__init__(x)
        self.n = n
        self.r = r

    @staticmethod
    def from_str(s):
        true_radical_pattern = "([0-9]+)^\(([0-9]+)/([0-9]+)\)"
        if re.match(true_radical_pattern, s):
            matcher = re.search(true_radical_pattern, s)
            return Radical(matcher.group(1), matcher.group(2), matcher.group(3))
        elif len(re.search("([0-9]+)", s).groups()) == 1:
            return Radical(int(s), 1, 1)

    def evaluate(self):
        return self.x ** (self.n / self.r)

    def show(self):
        if self.n == 1 and self.r == 1:
            return str(self.x)
        else:
            return str(self.x) + "^(" + str(self.n) + "/" + str(self.r) + ")"

    def __mul__(self, other):
        assert self.n == other.n and self.r == other.r
        return Radical(self.x * other.x, self.n, self.r)

    def __eq__(self, other):
        return self.x == other.x and self.n == other.n and self.r == other.r

    def __str__(self):
        return self.show()

    def __pow__(self, power, modulo=None):
        return Radical(self.x, power * self.n, self.r)