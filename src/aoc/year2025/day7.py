# Helper function
def print_pascal(splitters, beams, numbers):
    ymax = max(numbers)
    xmax = max(numbers[ymax])
    for y in range(ymax + 1):
        for x in range(xmax + 1):
            if x in beams.get(y, []):
                print("|", end="")
            elif x in splitters.get(y, []):
                print("^", end="")
            elif x in numbers.get(y, {}):
                print(f"{numbers[y][x]:0X}", end="")
            else:
                print(".", end="")
        print()


def read(fname=0):
    splitters = {}
    with open(fname) as file:
        for y, line in enumerate(file):
            if "^" in line:
                splitters[y] = {x for x, c in enumerate(line) if c == "^"}
            elif "S" in line:
                start = line.index("S")
    return start, splitters


def calc(start, splitters):
    beams = {start}
    # Uncomment for printing the Pascal triangle
    # allbeams = {0: {start}}
    n = 0
    pascal = {1: {start: 1}}
    for key, splitterline in splitters.items():
        newbeams = set()
        pkey = key + 1
        pascal[pkey] = pascal[pkey - 2].copy()
        for xpos in splitterline:
            if xpos in beams:
                n += 1
                beams.remove(xpos)
                newbeams.add(xpos - 1)
                newbeams.add(xpos + 1)
                previous = pascal[pkey - 2][xpos]
                pascal[pkey][xpos - 1] = pascal[pkey].get(xpos - 1, 0) + previous
                pascal[pkey][xpos + 1] = pascal[pkey].get(xpos + 1, 0) + previous
                del pascal[pkey][xpos]
        beams |= newbeams
        # Uncomment for printing the Pascal triangle
        # allbeams[key] = beams.copy()
    # print_pascal(splitters, allbeams, pascal)
    m = sum(pascal[pkey].values())
    return n, m


def run(fname=0):
    start, splitters = read(fname)
    n1, n2 = calc(start, splitters)
    return n1, n2


if __name__ == "__main__":
    import sys

    try:
        fname = sys.argv[1]
    except IndexError:
        fname = 0
    n1, n2 = run(fname)
    print(n1, n2)
