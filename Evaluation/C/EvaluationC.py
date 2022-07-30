from Evaluation.C.C import C
from Evaluation.QStar import base
from src.Solver import Solver

solver = Solver(C, base)
solver.gather_two_cocycle_candidates(attempts=10000, bound=200)
