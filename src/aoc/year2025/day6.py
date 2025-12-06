def read(fname=0):
    data = []
    with open(fname) as file:
        lines = [line.strip("\n") for line in file.readlines()]
    # Part 1
    for line in lines:
        items = line.strip().split()
        try:
            data.append([int(value) for value in items])
        except ValueError:
            ops = items
    data = zip(*data)
    # Part 2
    data2 = []
    lines = [line[::-1] for line in lines]
    # Grab the column positions from the operator symbols
    icols = [-2] + [i for i, c in enumerate(lines[-1]) if c != " "]
    # Step through each "wide" column
    for start, end in zip(icols[:-1], icols[1:]):
        # Store all row items in a single wide column
        cells = [line[start + 2 : end + 1] for line in lines[:-1]]
        # Step through the "narrow" columns
        # and combine the resulting string into a number
        numbers = [int("".join(chars)) for chars in zip(*cells)]
        data2.append(numbers)
    return data, data2, ops


def calc(data, ops):
    total = 0
    for op, numbers in zip(ops, data):
        # functools.reduce and operator.add/mult would
        # be more fun, but let's do without imports
        if op == "+":
            total += sum(numbers)
        if op == "*":
            value = 1
            for number in numbers:
                value *= number
            total += value
    return total


def run(fname=0):
    data, data2, ops = read(fname)
    n1 = calc(data, ops)
    n2 = calc(data2, ops[::-1])
    return n1, n2


if __name__ == "__main__":
    import sys

    try:
        fname = sys.argv[1]
    except IndexError:
        fname = 0
    n1, n2 = run(fname)
    print(n1, n2)
