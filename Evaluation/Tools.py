import multiprocessing
import threading
import time
from concurrent.futures import ThreadPoolExecutor

import numpy as np
from scipy.optimize import minimize


def print_opt_result(result):
    print(f"Success: {result.success}.\n"
          f"Minimum at \n"
          f"{result.x} \nwith message: \""
          f"{result.message}\" and value "
          f"{result.fun} after "
          f"{result.nit} iterations.")


def gather_starting_points(n, bound=1):
    starts = list()
    for _ in range(n):
        starts.append(np.random.rand(52))
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
    print("A calculation has started!")
    start = time.time()
    result = minimize(f, x0, method=method)
    duration = time.time() - start
    print(f"A calculation was successful, took {duration}s!")
    with open(file, "a") as file_object:
        file_object.write(str(result.x))
        file_object.write("\n")
        file_object.write(str(result.success))
        file_object.write("\n")
        file_object.write(str(result.fun))
        file_object.write("\n\n")
        file_object.close()


def gather_two_cocycles_mp(f, method="Powell", file="twococycles"):
    while True:
        starts = gather_starting_points(multiprocessing.cpu_count(), 4)
        with ThreadPoolExecutor() as executor:
            executor.map(
                lambda x: minimize_and_save(f, x, method, file + str(threading.get_native_id())),
                starts)


def gather_two_cocycles(f, method="Powell", file="twococycles"):
    while True:
        start = gather_starting_points(1, 5)[0]
        minimize_and_save(f, start, method, file)
