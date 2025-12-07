from pathlib import Path


def test_day1():
    from aoc.year2025 import day1

    fname = Path(__file__).parent / "data" / "2025" / "day1.in"
    results = day1.run(fname)
    assert results == (3, 6)


def test_day2():
    from aoc.year2025 import day2

    fname = Path(__file__).parent / "data" / "2025" / "day2.in"
    results = day2.run(fname)
    assert results == (1227775554, 4174379265)


def test_day2b():
    from aoc.year2025 import day2b

    fname = Path(__file__).parent / "data" / "2025" / "day2.in"
    results = day2b.run(fname)
    assert results == (1227775554, 4174379265)


def test_day3():
    from aoc.year2025 import day3

    fname = Path(__file__).parent / "data" / "2025" / "day3.in"
    results = day3.run(fname)
    assert results == (357, 3121910778619)


def test_day4():
    from aoc.year2025 import day4

    fname = Path(__file__).parent / "data" / "2025" / "day4.in"
    results = day4.run(fname)
    assert results == (13, 43)


def test_day4b():
    from aoc.year2025 import day4b

    fname = Path(__file__).parent / "data" / "2025" / "day4.in"
    results = day4b.run(fname)
    assert results == (13, 43)


def test_day5():
    from aoc.year2025 import day5

    fname = Path(__file__).parent / "data" / "2025" / "day5.in"
    results = day5.run(fname)
    assert results == (3, 14)


def test_day6():
    from aoc.year2025 import day6

    fname = Path(__file__).parent / "data" / "2025" / "day6.in"
    results = day6.run(fname)
    assert results == (4277556, 3263827)


def test_day6b():
    from aoc.year2025 import day6b

    fname = Path(__file__).parent / "data" / "2025" / "day6.in"
    results = day6b.run(fname)
    assert results == (4277556, 3263827)


def test_day7():
    from aoc.year2025 import day7

    fname = Path(__file__).parent / "data" / "2025" / "day7.in"
    results = day7.run(fname)
    assert results == (21, 40)
