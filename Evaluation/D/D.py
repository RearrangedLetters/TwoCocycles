###
# Represents the group of automorphisms of the field extension of Q
# by a cube root of 2.
###
from Evaluation.QStar import *
from src.Group import Group

elements = (id, d, d2)

cayley_table = [[0, 1, 2],
                [1, 2, 0],
                [2, 0, 1]]

D = Group(elements, cayley_table)
