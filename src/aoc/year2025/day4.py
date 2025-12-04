def printgrid(grid, xmax, ymax, use_symbols=False):
    for x in range(-1, xmax + 1):
        for y in range(-1, ymax + 1):
            if use_symbols:
                print("@."[grid[(x, y)]])
            else:
                print(grid[(x, y)])


def addborder(grid, xmax, ymax):
    for x in range(-1, xmax + 1):
        grid[(x, -1)] = 0
        grid[(x, ymax)] = 0
    for y in range(-1, ymax + 1):
        grid[(-1, y)] = 0
        grid[(xmax, y)] = 0


def read(fname):
    grid = {}
    valid = {}
    for y, line in enumerate(open(fname)):
        line = line.strip()
        xmax = len(line)
        for x, cell in enumerate(line):
            grid[(x, y)] = int(cell == "@")
            if grid[(x, y)]:
                valid[(x, y)] = 1
    ymax = y + 1
    addborder(grid, xmax, ymax)
    return grid, valid


def solve(grid, valid):
    neighbours = {}
    for x, y in valid:
        neighbours[(x, y)] = -1
        for dx in -1, 0, 1:
            for dy in -1, 0, 1:
                neighbours[(x, y)] += grid[(x + dx, y + dy)]
    return [pos for pos, nrolls in neighbours.items() if nrolls < 4]


def calc(fname):
    grid, valid = read(fname)

    total1 = len(solve(grid, valid))
    total2 = 0
    l = 1
    while l:
        poses = solve(grid, valid)
        l = len(poses)
        total2 += l
        for pos in poses:
            grid[pos] = 0
            del valid[pos]
    return total1, total2


def run(fname=0, silent=False):
    total1, total2 = calc(fname)
    return total1, total2


if __name__ == "__main__":
    import sys

    try:
        fname = sys.argv[1]
    except IndexError:
        fname = 0
    n1, n2 = run(fname)
    print(n1, n2)
