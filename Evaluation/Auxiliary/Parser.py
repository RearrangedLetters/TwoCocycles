from Evaluation.Auxiliary.Reformatting import two_cocycle_from_flat, two_cocycle_from_flat_simplified


def parse_two_cocycles(group, base, file="two_cocycles"):
    with open(file) as f:
        lines = f.readlines()
    two_cocycles = list()
    for i in range(0, len(lines), 3):
        x = lines[i].split(";")
        two_cocycles.append(two_cocycle_from_flat(x, group, base))
    return two_cocycles


def parse_two_cocycles_simplified(group, base, positions, file="two_cocycles_simplified"):
    with open(file) as f:
        lines = f.readlines()
    two_cocycles = list()
    for i in range(0, len(lines), 3):
        x = lines[i].split(";")
        two_cocycles.append(two_cocycle_from_flat_simplified(x, group, base, positions))
    return two_cocycles


def count_empty(file="two_cocycles"):
    count = 0
    with open(file) as f:
        for line in f:
            if not line.strip():
                count += 1
    return count