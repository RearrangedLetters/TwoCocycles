import numpy as np
from scipy.optimize import fsolve


f = lambda x: x**3 - 100*x**2 + 100
print(fsolve(f, np.ndarray([1, 80])))
