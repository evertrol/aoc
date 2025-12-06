# Values to safely skip ahead if we found a repeating pattern,
# depending on the number of digits
# Note the lower value for 6 digits: after a 3-3 match,
# a 2-2-2 match can occur 91 values later, e.g.
# 565 565 + 91 = 56 56 56. Something similar is the case
# for 10 digits: 65 65 65 65 65 + 9091 = 65656 65656
NSKIP = {4: 99, 6: 90, 8: 9999, 9: 1_001_000, 10: 9090}


def calcpair(low, high):
    n1 = n2 = 0
    low = max(low, 10)
    i = low
    while i <= high:
        s = str(i)
        l = len(s)
        ls = len(set(s))
        if ls == 1:  # single repeating digit
            n2 += i
            if l % 2 == 0:
                n1 += i
        # the number of unique digits are at most half the length of
        # the full number
        elif ls <= l / 2 + 1:
            for ll in range(l // 2, 1, -1):
                if l % ll:  # not exactly divisible: can't fully repeat
                    continue
                nl = l // ll
                if s == s[:ll] * nl:
                    n2 += i
                    if nl == 2:
                        n1 += i
                    # bail out early to prevent multiple inclusions of
                    # numbers like 12121212, which is 12 12 12 12 and
                    # 1212 1212
                    #
                    # Skip a bunch of numbers, depending on the size
                    # of the shortest possible substring: `shortest`
                    #
                    # Also account for the `i += 1` at the bottom
                    # NB: these numbers are taken from estimates with
                    # example ranges
                    i += NSKIP[l]
                    break
        i += 1
    return n1, n2


def run(fname=0):
    total1 = total2 = 0
    for low, high in [
        (int(value) for value in pair.split("-"))
        for pair in open(fname).read().strip().split(",")
    ]:
        n1, n2 = calcpair(low, high)
        total1 += n1
        total2 += n2
    return total1, total2


if __name__ == "__main__":
    import sys

    try:
        fname = sys.argv[1]
    except IndexError:
        fname = 0
    n1, n2 = run(fname)
    print(n1, n2)
