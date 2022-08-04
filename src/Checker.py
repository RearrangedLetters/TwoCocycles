import subprocess

from Evaluation.Auxiliary.Parser import parse_two_cocycles_simplified
from Evaluation.Auxiliary.Reformatting import to_pure_python
from Evaluation.G.G import G
from Evaluation.QStar import Q_star

cayley_table = G.cayley_table
order = len(G.elements)
file = "../Evaluation/G/two_cocycles_simplified_p(0, 3)"
two_cocycle = parse_two_cocycles_simplified(G, Q_star.base, (0, 3), file)[0]
mapping = to_pure_python(two_cocycle.mapping)

sage_code = f"""
Q.<theta, omega> = NumberField([x^3 - 2, x^2 + x + 1])
base = (1, theta, theta ** 2, omega, omega * theta, omega * theta ** 2)
order = len(base)
cayley_table = {cayley_table}

delta = Rational((212305962435342, 34732938946034532445))
gamma = Rational((23183275331455435, 234235864325))
ext(q) = [q, Rational(0), Rational(0), Rational(0), Rational(0), Rational(0)]
one = ext(1)
gammadelta = ext(gamma * delta)
delta = ext(delta)
gamma = ext(gamma)

mapping = [[one, one, one, one, one, one],
           [one, one, delta, one, one, delta],
           [one, delta, delta, one, delta, delta],
           [one, one, one, gamma, gamma, gamma],
           [one, one, delta, gamma, gamma, gammadelta],
           [one, delta, delta, gamma, gammadelta, gammadelta]]

# mapping = {mapping}

def eval_vec(x):
    result = 0
    for i, xi in enumerate(x):
        result = result + Rational(xi) * base[i]
    return result

def id(x):
    return x

def d(x):
    return [x[0], -x[4], x[5] - x[2], x[3], x[1] - x[4], -x[2]]

def c(x):
    return [x[0] - x[3], x[1] - x[4], x[2] - x[5], -x[3], -x[4], -x[5]]

elements = (id, d, lambda x: d(d(x)), c, lambda x: c(d(x)), lambda x: c(d(d(x))))

def evaluate_left(g, h, k):
    return eval_vec(mapping[g][h]) * eval_vec(mapping[cayley_table[g][h]][k])

def evaluate_right(g, h, k):
    group_op = elements[g]
    return eval_vec(group_op(mapping[h][k])) * eval_vec(mapping[g][cayley_table[h][k]])

def evaluate(g, h, k):
    return evaluate_left(g, h, k) - evaluate_right(g, h, k)

def summed_difference():
    sum = 0
    for g in range(order):
        for h in range(order):
            for k in range(order):
                sum = sum + evaluate(g, h, k)
    return sum / order ** 3

# print(summed_difference().abs(prec=1000))
print(summed_difference())
"""


result = subprocess.run(["sage", "-c", sage_code], stdout=subprocess.PIPE)
print(result.stdout.decode("utf-8"))
