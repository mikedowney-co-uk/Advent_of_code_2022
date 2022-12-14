from aoc import aoc
from functools import cmp_to_key


def parse(lines):
    pairs = []
    pair = []
    for line in lines:
        if line != "":
            pair.append(eval(line))
        else:
            pairs.append(pair)
            pair = []
    if len(pair) == 2:
        pairs.append(pair)
    return pairs


def compareint(left, right):
    if left == right:
        return 0
    else:
        return -1 if left < right else 1


def compare(left, right):
    if type(left) == int and type(right) == int:
        return compareint(left, right)
    if type(left) == int:
        left = [left]
    if type(right) == int:
        right = [right]
    return comparelists(left, right)


def comparelists(a, b):
    for left, right in zip(a, b):
        c = compare(left, right)
        if c == 0:
            continue
        return c

    # Everything matches, so check list size
    if len(a) == len(b):
        return 0
    else:
        return -1 if len(a) < len(b) else 1


def part1(pairs):
    inorder = []
    for i, p in enumerate(pairs):
        if compare(*p) == -1:
            inorder.append(1 + i)
    result = sum(inorder)
    assert result == 13 or result == 6428
    return result


def part2(pairs):
    packets = [p for pair in pairs for p in pair]
    packets.extend([[[2]], [[6]]])
    packets = sorted(packets, key=cmp_to_key(compare))
    div1 = 1 + packets.index([[2]])
    div2 = 1 + packets.index([[6]])
    result = div1 * div2
    assert result == 140 or result == 22464
    return result


def run(file):
    print("Part 1")
    data = aoc.loadlines(file)
    pairs = parse(data)
    print(part1(pairs))
    print("Part 2")
    print(part2(pairs))


if __name__ == "__main__":
    print("Test Data")
    run("test.txt")
    print("Actual Data")
    run("data.txt")
    exit()
