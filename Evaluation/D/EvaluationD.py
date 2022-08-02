from Evaluation.Auxiliary.Parser import parse_two_cocycles_simplified
from Evaluation.Auxiliary.Plotting import grid_plot
from Evaluation.D.D import D
from Evaluation.QStar import base, Q_star
from src.Solver import Solver

solver = Solver(D, base)
solver.gather_two_cocycle_candidates_simplified(positions=(0, 3), attempts=20, bound=2)

grid_plot(parse_two_cocycles_simplified(D, Q_star.base, (0, 3), "../D/two_cocycles_simplified_p(0, 3)")[:10])
