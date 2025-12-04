import timeit

number = 50
for day in 1, 2, 3, 4:
    module = f"day{day}"
    fname = f"day{day}.in"
    print(f"day {day}", end=": ")
    timer = timeit.Timer(f"run('{fname}', silent=True)", setup=f"from {module} import run")
    print(timer.timeit(number=number)/number * 1000, "ms")
