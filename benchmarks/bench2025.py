import sys
import timeit

try:
    template = sys.argv[1]
except IndexError:
    print(f"Usage: {sys.argv[0]} <filename> [repeat] [n]", file=sys.stderr)
    exit(1)

repeat = 5
try:
    repeat = int(sys.argv[2])
except IndexError:
    pass
except ValueError:
    print("<repeat> should be an integer", file=sys.stderr)
    exit(1)
if repeat < 1:
    print("<repeat> should be a positive integer", file=sys.stderr)
    exit(1)

number = 5
try:
    number = int(sys.argv[3])
except IndexError:
    pass
except ValueError:
    print("<n> should be an integer", file=sys.stderr)
    exit(1)
if number < 1:
    print("<n> should be a positive integer", file=sys.stderr)
    exit(1)


for day in 1, 2, 3, 4, 5, 6:
    module = f"aoc.year2025.day{day}"
    fname = template[::-1].replace("0", f"{day}", 1)[::-1]
    print(f"day {day}:")
    timer = timeit.Timer(f"run('{fname}')", setup=f"from {module} import run")
    results = timer.repeat(repeat=repeat, number=number)
    results = [result / number for result in results]
    print(f"  min = {min(results) * 1000} ms")
    print(f"  max = {max(results) * 1000} ms")
    print(f"  average = {sum(results) / repeat * 1000} ms")
    results.sort()
    median = (
        results[repeat // 2]
        if repeat % 2
        else (results[repeat // 2 - 1] + results[repeat // 2]) / 2
    )
    print(f"  median = {median * 1000} ms")
