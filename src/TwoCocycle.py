class TwoCocycle:
    def __init__(self, group, base, mapping):
        self.group = group
        self.base = base
        self.mapping = mapping

    def evaluate(self, g, h):
        return self.mapping[g][h]
