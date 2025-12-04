def read(fname=0):
    intervals = []
    idents = []
    with open(fname) as file:
        for line in file:
            line = line.strip()
            if "-" in line:
                interval = tuple(int(value) for value in line.split("-"))
                intervals.append(interval)
            elif line:
                idents.append(int(line))
    return intervals, idents


def combine(intervals):
    intervals.sort(key=lambda interval: interval[0])

    newintervals = []
    interval1 = intervals[0]
    newintervals.append(interval1)
    n = len(intervals)
    i = 1
    while i < n:
        interval2 = intervals[i]
        if interval2[0] <= interval1[1]:
            if interval2[1] > interval1[1]:
                interval1 = (interval1[0], interval2[1])
            newintervals[-1] = interval1
        else:
            interval1 = interval2
            newintervals.append(interval1)
        i += 1
    return newintervals


def calc(intervals, idents):
    intervals = combine(intervals)

    total2 = sum(interval[1] - interval[0] + 1 for interval in intervals)

    fresh = []
    for ident in idents:
        for interval in intervals:
            if interval[0] <= ident <= interval[1] + 1:
                fresh.append(ident)
                break
    total1 = len(fresh)

    return total1, total2


def run(fname=0):
    intervals, idents = read(fname)
    total1, total2 = calc(intervals, idents)
    return total1, total2


if __name__ == "__main__":
    import sys

    try:
        fname = sys.argv[1]
    except IndexError:
        fname = 0
    n1, n2 = run(fname)
    print(n1, n2)
