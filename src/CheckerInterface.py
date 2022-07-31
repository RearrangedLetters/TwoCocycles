import subprocess

from Evaluation.G.G import G

cayley_table = G.cayley_table
order = len(G.elements)
mapping = list()

sage_code = f"""
Q.<theta, omega> = NumberField([x^3 - 2, x^2 + x + 1])
base = (1, theta, theta ** 2, omega, omega * theta, omega * theta ** 2)
order = len(base)
# cayley_table = {cayley_table}
cayley_table = [[0, 1, 2, 3, 4, 5],
                [1, 2, 0, 5, 3, 4],
                [2, 0, 1, 4, 5, 3],
                [3, 4, 5, 0, 1, 2],
                [4, 5, 3, 2, 0, 1],
                [5, 3, 4, 1, 2, 0]]
delta = Rational(2)
gamma = Rational(1)

ext(q) = [q, Rational(0), Rational(0), Rational(0), Rational(0), Rational(0)]
one = ext(1)
deltagamma = ext(delta * gamma)
delta = ext(delta)
gamma = ext(gamma)

mapping = [[one, one, delta, gamma, gamma, deltagamma],
           [one, delta, delta, gamma, deltagamma, deltagamma],
           [delta, delta, delta, deltagamma, deltagamma, deltagamma],
           [gamma, gamma, deltagamma, gamma, gamma, deltagamma],
           [gamma, deltagamma, deltagamma, gamma, deltagamma, deltagamma],
           [deltagamma, deltagamma, deltagamma, deltagamma, deltagamma, deltagamma]]

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
                sum = sum + evaluate(g, h, k).norm()
    return sum / order ** 3

print(summed_difference())
# print(eval_vec([1, 1, 1, 1, 1, 1]))
# print(Rational(deltagamma[0]) * omega)
"""


result = subprocess.run(["sage", "-c", sage_code], stdout=subprocess.PIPE)
print(result.stdout.decode("utf-8"))

