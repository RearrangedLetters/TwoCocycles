class TwoCocycle:
    def __init__(self, base, mapping):
        self.base = base
        self.mapping = mapping

    def apply(self, g, h):
        return self.mapping[g][h]
