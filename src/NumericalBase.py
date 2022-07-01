class NumericalBase:

    def __init__(self, base):
        self.base = base


def eval(B, vector):
    result = 0
    for i, b in enumerate(B):
        result = result + b * vector[i]
    return result
