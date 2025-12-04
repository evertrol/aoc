def calc(fname=0):
    clicks = rot = 0
    dial = 50
    for line in open(fname):
        n = int(line[1:])
        clicks += n // 100
        n %= 100
        if line[0] == "L":
            n = -n
        dial += n
        if dial != n:
            if dial > 100 or dial < 0:
                clicks += 1
        dial %= 100
        if dial == 0:
            rot += 1
            clicks += 1
    return rot, clicks


def run(fname=0):
    rot, clicks = calc(fname)
    return rot, clicks


if __name__ == "__main__":
    import sys

    try:
        fname = sys.argv[1]
    except IndexError:
        fname = 0
    n1, n2 = run(fname)
    print(n1, n2)
