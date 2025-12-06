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
                valid[(x, y)] = 9
    ymax = y + 1
    addborder(grid, xmax, ymax)
    return grid, valid


def solve(grid, valid):
    for x, y in valid:
        valid[(x, y)] = -1
        for dx in -1, 0, 1:
            for dy in -1, 0, 1:
                valid[(x, y)] += grid[(x + dx, y + dy)]


def update(grid, valid):
    # Remove now invalid grid positions
    n = len(valid)
    for pos, nneighbours in valid.copy().items():
        if nneighbours < 4:
            grid[pos] = 0
            del valid[pos]
    return n - len(valid)


def calc(fname):
    grid, valid = read(fname)
    solve(grid, valid)
    total1 = total2 = update(grid, valid)
    while True:
        solve(grid, valid)
        n = update(grid, valid)
        if not n:
            break
        total2 += n
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
