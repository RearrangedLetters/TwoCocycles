import multiprocessing
import threading
import time
from concurrent.futures import ThreadPoolExecutor

import numpy as np
from scipy.optimize import minimize

from src import Norms


def print_opt_result(result):
    print(f"Success: {result.success}.\n"
          f"Minimum at \n"
          f"{result.x} \nwith message: \""
          f"{result.message}\" and value "
          f"{result.fun} after "
          f"{result.nit} iterations.")


def gather_starting_points(n, k, bound=1):
    starts = list()
    for _ in range(n):
        starts.append(np.random.rand(k))
    return np.array([x * bound for x in starts])


def eval_and_save(fun, x, file):
    with open(file, "a") as file_object:
        file_object.write(fun(x))
        file_object.write("\n")


def minimize_from(f, x0, method):
    result = minimize(f, x0, method=method)
    print("A calculation was successful!")
    return result.x, result.success


def minimize_and_save(f, x0, method, file):
    start = time.time()
    result = minimize(f, x0, method=method)
    duration = time.time() - start
    print(f"A calculation was successful, took {duration}s!")
    R = result.x[:-2]
    q = result.x[-2:]
    if Norms.euclidean(R) > 1e-2 and Norms.euclidean(q) > 1e-3:
        with open(file, "a") as file_object:
            file_object.write(str(result.x))
            file_object.write("\n")
            file_object.write(str(result.success))
            file_object.write("\n")
            file_object.write(str(result.fun))
            file_object.write("\n\n")
            file_object.close()
        return True
    else:
        return False


def gather_two_cocycles_mp(f, method="Powell", file="twococycles"):
    while True:
        starts = gather_starting_points(multiprocessing.cpu_count(), 4)
        with ThreadPoolExecutor() as executor:
            executor.map(
                lambda x: minimize_and_save(f, x, method, file + str(threading.get_native_id())),
                starts)


def gather_two_cocycles(f, k, num=1000, bound=5, method="Powell", file="twococycles"):
    count = 0
    while count < num:
        start = gather_starting_points(1, k, bound)[0]
        is_nonzero = minimize_and_save(f, start, method, file)
        if is_nonzero:
            count = count + 1
            print(f"Found {count} out of {num}")
