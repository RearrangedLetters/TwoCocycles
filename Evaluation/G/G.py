###
# The Galois group G of Q_* over Q.
###
from src.Group import Group
from Evaluation.QStar import Q_star

cayley_table = [[0, 1, 2, 3, 4, 5],
                [1, 2, 0, 5, 3, 4],
                [2, 0, 1, 4, 5, 3],
                [3, 4, 5, 0, 1, 2],
                [4, 5, 3, 2, 0, 1],
                [5, 3, 4, 1, 2, 0]]

G = Group(Q_star.field_automorphisms, cayley_table)
