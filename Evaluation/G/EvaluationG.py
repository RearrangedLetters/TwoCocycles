from Evaluation.Auxiliary.Parser import parse_two_cocycles_simplified
from Evaluation.Auxiliary.Plotting import grid_plot
from Evaluation.G.G import G
from Evaluation.QStar import base, Q_star
from src.Solver import Solver

solver = Solver(G, base, zero_range=1e-2, max_error=1e-5)
# solver.gather_two_cocycle_candidates(attempts=1, bound=2)
solver.gather_two_cocycle_candidates_simplified(positions=(0, 3), attempts=30, bound=2)

grid_plot(parse_two_cocycles_simplified(G, Q_star.base, (0, 3), "../G/two_cocycles_simplified_p(0, 3)")[:10])
