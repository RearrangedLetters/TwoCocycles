from Evaluation.G.TwoCocycleG import summed_difference_var
from Evaluation.Tools import gather_two_cocycles

f = summed_difference_var

gather_two_cocycles(f, 52, num=100, bound=1, method="BFGS")
