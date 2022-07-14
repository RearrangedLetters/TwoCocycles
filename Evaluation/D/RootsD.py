from Evaluation.Tools import gather_two_cocycles
from TwoCocycleD import summed_difference_var

f = summed_difference_var

gather_two_cocycles(f, 10, num=1000, bound=4, method="BFGS")