from Evaluation.D.D import D
from Evaluation.QStar import base
from src.Solver import Solver

solver = Solver(D, base)
solver.gather_two_cocycle_candidates_simplified(positions=(0,2), attempts=10, bound=2)
