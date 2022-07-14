from Evaluation.Tools import gather_two_cocycles
from TwoCocycleC import summed_difference_var

f = summed_difference_var

gather_two_cocycles(f, 4, num=900, bound=10, method="BFGS")