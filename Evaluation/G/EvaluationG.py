from Evaluation.G.G import G
from Evaluation.QStar import base
from src.Solver import Solver

solver = Solver(G, base, max_error=1e-5)
solver.gather_two_cocycle_candidates(attempts=100, bound=2)

# grid_plot(parse_roots(26, "../Evaluation/G/twococycles"), 6)
