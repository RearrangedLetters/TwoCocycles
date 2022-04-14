def array_to_method(a):
    def f(x):
        return a(x)
    return f


def permutation_to_method(p):
    return array_to_method(p)

