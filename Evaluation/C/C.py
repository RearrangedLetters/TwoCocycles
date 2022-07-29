###
# Represents the group of automorphisms of the field extension of Q
# by a third root of unity.
###
from Evaluation.QStar import *
from src.Group import Group

elements = (id, c)

cayley_table = [[0, 1],
                [1, 0]]

C = Group(elements, cayley_table)
