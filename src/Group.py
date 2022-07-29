class Group:
    def __init__(self, elements, cayley_table):
        self.elements = elements
        self.cayley_table = cayley_table

    def op(self, x, y):
        return self.cayley_table[x][y]