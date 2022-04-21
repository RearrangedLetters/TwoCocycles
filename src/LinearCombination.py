class LinearCombination:
    def __init__(self, base, scalars):
        assert len(base) == len(scalars)
        self.base = base
        self.scalars = scalars

    def set_scalar(self, value, position):
        self.scalars[position] = value

    def set_scalars(self, scalars):
        self.scalars = scalars

    def get_scalar(self, position):
        return self.scalars[position]

    def get_scalars(self):
        return self.scalars

    def get_base_vector(self, position):
        return self.base[position]

    def get_base(self):
        return self.base

    def set_base(self, base):
        self.base = base

    def apply_to_base(self, f):
        C = list()
        for b in self.base:
            c = f(b)
            C.append(c)
        self.base = C

    def evaluate(self):
        value = 0
        for i in range(len(self.base)):
            value = value + self.scalars[i].evaluate() * self.base[i].evaluate()
        return value

    def show(self):
        s = self.scalars[0].show() + "*" + self.base[0].show()
        for i in range(1, len(self.base)):
            s = s + "+" + self.scalars[i].show() + "*" + self.base[i].show()
        return s
