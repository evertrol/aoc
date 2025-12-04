This repository contains solutions to Advent of Code problems.

The solutions are coded as individual modules in a Python package called `aoc`. If you install it, then the modules are called `aoc.year2025.day1`, `aoc.year2025.day2` and so on (currently, only 2025 is available).

## Installation

You can install the package simply with

```shell
pip install git+https://github.com/evertrol/aoc.git
```

in a virtual environment or directly as a user installation (in `.local/` in your home directory).

There are no external dependencies.

## Usage

To run a solution, run the module, as follows:

```shell
python -m aoc.year2025.day1 day1.in
```

where `day1.in` is your input data file. You can also use redirection, i.e.,

```shell
python -m aoc.year2025.day1 < day1.in
```

## Benchmarks

If you like timings, you can run some benchmarks. These are done using the `timeit` module.

Provide your own input data; or use the test data, but this will have limited functionality, since it is relatively small.

The `benchmarks/run.sh` gives an example how to run the benchmarks. The arguments to `bench2025.py` are as follows:

- a "template" file for the input data, where the `0` is replaced by the relevant day. The available days are listed in `bench2025.py` itself, in the for loop. All relevant files should be available, at the same path as the template argument, with the `0` replaced by the corresponding day number. Note that it is assumed that are no other `0`s following the the day number (but `0`s before are ok: replacement is done from the end, for only the last `0`).

- a number of repeats; a positive integer. This is used to get multiple timings for the statistics, to calculate a minimum and maximum duration, as well as a mean and median. See the `repeat` argument for `timeit`. The default is 5.

- a number of times to run. This is just averaged, and then considered one repeat. The default is 5.

The total number of times the benchmarked code is run is thus `repeat` * `number`.


### Single benchmark

If you want to run a single benchmark, use the `benchmarks/bench.py` script, as follows:

```
python benchmarks/bench.py <module-name> <data-file> [repeat] [n]
```

where `<module-name>` is the full module name in dotted form, e.g. `aoc.year2025.day4`. For example,

```
python benchmarks/bench.py aoc.year2025.day4 day4.input
```

All other arguments have the same meaning as for the `bench2025.py` script, and the same defaults for `repeat` and `n`.
