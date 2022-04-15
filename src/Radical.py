from src.Number import Number


###
# Represents a radical. If x is the radicand which is raised to the n-the power
# and we take the r-th root. Then this class represents x^(n/r)
###
class Radical(Number):
    def __init__(self, x, n, r):
        super().__init__(x)
        self.n = n
        self.r = r

    def evaluate(self):
        return self.x ** (self.n / self.r)

    def show(self):
        return str(self.x) + "(" + str(self.n) + "/" + str(self.r) + ")"
