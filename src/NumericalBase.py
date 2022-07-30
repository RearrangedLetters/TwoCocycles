class NumericalBase:
    def __init__(self, base):
        self.base = base

    def evaluate(self, vector):
        result = 0
        for i, b in enumerate(self.base):
            result = result + b * vector[i]
        return result
