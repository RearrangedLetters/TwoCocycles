class Vector:

    def __init__(self, base, vector):
        self.base = base
        self.vector = vector

    def eval(self):
        result = 0
        for i, x in enumerate(self.vector):
            result = result + x * self.base[i]
        return result
