import sys
import timeit

try:
    module = sys.argv[1]
    fname = sys.argv[2]
except IndexError:
    print(
        f"Usage: {sys.argv[0]} <module-name> <data-file> [repeat] [n]", file=sys.stderr
    )
    exit(1)

repeat = 5
try:
    repeat = int(sys.argv[3])
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
    number = int(sys.argv[4])
except IndexError:
    pass
except ValueError:
    print("<n> should be an integer", file=sys.stderr)
    exit(1)
if number < 1:
    print("<n> should be a positive integer", file=sys.stderr)
    exit(1)


print(f"{module}:")
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
