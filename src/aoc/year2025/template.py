def read(fname=0):
    with open(fname) as file:
        for line in file:
            line = line.strip()
    return None


def calc(data):
    return 0, 0


def run(fname=0):
    data = read(fname)
    n1, n2 = calc(data)
    return n1, n2


if __name__ == "__main__":
    import sys

    try:
        fname = sys.argv[1]
    except IndexError:
        fname = 0
    n1, n2 = run(fname)
    print(n1, n2)
