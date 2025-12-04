def calc(lines, level):
    total = 0
    for line in lines:
        n = 0
        l = len(line)
        joltage = ""
        s = 0
        for n in range(level, 0, -1):
            for d in "987654321":
                try:
                    b = line[s : l - n].index(d)
                    joltage += d
                    s = s + b + 1
                    break
                except ValueError:
                    continue
        total += int(joltage)
    return total


def run(fname=0):
    lines = open(fname).readlines()
    total = {}
    for level in [2, 12]:
        total[level] = calc(lines, level)
    return total[2], total[12]


if __name__ == "__main__":
    import sys

    try:
        fname = sys.argv[1]
    except IndexError:
        fname = 0
    n1, n2 = run(fname)
    print(n1, n2)
