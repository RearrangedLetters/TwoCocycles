###
# Represents the group of automorphisms of the field extension of Q
# by a third root of unity.
###
from src import RootOfUnity
from src.FieldAutomorphism import FieldAutomorphism
from src.NumericalBase import NumericalBase

B = NumericalBase([1, RootOfUnity.root_of_unity(3), 1, 1, 1, 1])  # todo: This is probably the wrong base

l_identity = lambda x: x
identity = FieldAutomorphism(B, [l_identity, l_identity, l_identity, l_identity, l_identity, l_identity])
conjugation = FieldAutomorphism(B, [l_identity, lambda x: -x, l_identity, l_identity, l_identity, l_identity])

G = (identity,
     conjugation,
     identity,
     identity,
     identity,
     identity)

composition_table_functions = [[identity, conjugation, identity, identity, identity, identity],
                               [conjugation, identity, identity, identity, identity, identity],
                               [identity, identity, identity, identity, identity, identity],
                               [identity, identity, identity, identity, identity, identity],
                               [identity, identity, identity, identity, identity, identity],
                               [identity, identity, identity, identity, identity, identity]]

composition_table = [[0, 1, 0, 0, 0, 0],
                     [1, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0]]
