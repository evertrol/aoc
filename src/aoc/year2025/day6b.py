def read(fname=0):
    with open(fname) as file:
        lines = [line.strip("\n") for line in file]
    return lines


def add_mult(op, numbers):
    # functools.reduce and operator.add/mult would
    # be more fun, or even math.prod,
    # but let's do without imports
    if op == "+":
        value = sum(numbers)
    if op == "*":
        value = 1
        for number in numbers:
            value *= number
    return value


def calc(lines):
    total1 = total2 = 0
    ops = lines[-1].split()
    lines = lines[:-1]
    data = (map(int, line.split()) for line in lines)
    data = zip(*data)
    for op, numbers in zip(ops, data):
        total1 += add_mult(op, numbers)
    data = []
    numbers = []
    for column in zip(*lines):
        column = "".join(column).strip()
        if column:
            numbers.append(int(column))
        else:
            data.append(numbers)
            numbers = []
    data.append(numbers)
    for op, numbers in zip(ops, data):
        total2 += add_mult(op, numbers)

    return total1, total2


def run(fname=0):
    lines = read(fname)
    n1, n2 = calc(lines)
    return n1, n2


if __name__ == "__main__":
    import sys

    try:
        fname = sys.argv[1]
    except IndexError:
        fname = 0
    n1, n2 = run(fname)
    print(n1, n2)
