def read(fname=0):
    boxes = []
    with open(fname) as file:
        for line in file:
            line = line.strip()
            boxes.append([int(value) for value in line.split(",")])
    return boxes


def calc(boxes):
    n = len(boxes)
    # When to calculate the solution to the first part
    itestpair = 10 if n < 100 else 1000
    distances = []
    for i, box in enumerate(boxes):
        x, y, z = box
        distances.extend(
            [
                (((x - x2) ** 2 + (y - y2) ** 2 + (z - z2) ** 2), (i, j + i + 1))
                for j, (x2, y2, z2) in enumerate(boxes[i + 1 :])
            ]
        )
    distance, (i, j) = distances[-1]
    distances.sort()
    circuits = []
    for ipair, (distance, pair) in enumerate(distances):
        if ipair == itestpair:  # calculate solution to the first part
            sizes = [len(circuit) for circuit in circuits]
            sizes = list(reversed(sorted(sizes)))
            prod = sizes[0] * sizes[1] * sizes[2]

        i, j = pair
        for k, circuit in enumerate(circuits):
            if i in circuit:
                circuits[k].add(j)
                break
            if j in circuit:
                circuits[k].add(i)
                break
        else:
            circuits.append({i, j})
            k = len(circuits) - 1
        # Check if the latest change created two
        # circuits with a common junction box
        test_circuit = circuits[k]  # changed circuit
        common = []
        for l, circuit in enumerate(circuits):
            if circuit == test_circuit:
                continue
            if circuit & test_circuit:
                common.append(l)
        if common:
            for l in common:
                circuits[k] |= circuits[l]
            for l in common:
                circuits.pop(l)
        if len(circuits) == 1 and len(circuits[0]) == n:
            prodx = boxes[i][0] * boxes[j][0]
            break

    return prod, prodx


def run(fname=0):
    data = read(fname)
    n1, n2 = calc(data)
    return n1, n2


if __name__ == "__main__":
    import sys

    try:
        fname = sys.argv[1]
    except IndexError:
        fname = 0
    n1, n2 = run(fname)
    print(n1, n2)
