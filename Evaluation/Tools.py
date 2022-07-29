import multiprocessing
import threading
import time
from concurrent.futures import ThreadPoolExecutor

from scipy.optimize import minimize

from Evaluation.Auxiliary.Parser import twococycle_from_root, twococycle_from_optimize_result
from Evaluation.G.GroupG import *
from Evaluation.QStar import B
from src import Norms
from src.TwoCocycleTools import TwoCocycleCondition


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


def minimize_and_save(f, x0, method, file, threshold=1e-3):
    start = time.time()
    result = minimize(f, x0, method=method, options={"ftol": 1e-6, "maxiter": len(x0) * 200})
    duration = time.time() - start
    print(f"\nA calculation has completed, took {duration}s")
    for i in range(0, len(result.x) - 1, 2):
        if Norms.euclidean([result.x[i], result.x[i + 1]]) < threshold:
            print("Solution declined, is 0 somewhere")
            return False

    twococycle = twococycle_from_optimize_result(result)
    condition = TwoCocycleCondition(B)
    error = condition.summed_difference(G, cayley_table=cayley_table,
                                        two_cocycle=twococycle, norm=Norms.complex_euclidean)

    if error < 1e-4:
        with open(file, "a") as file_object:
            file_object.write(str(result.x))
            file_object.write("\n")
            file_object.write(str(result.success))
            file_object.write("\n")
            file_object.write(str(error))
            file_object.write("\n\n")
            file_object.close()
        print("A result has been saved!")
        return True
    else:
        print("Accuracy was not achieved, average error is: " + str(error))
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
