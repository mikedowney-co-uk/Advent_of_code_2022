from aoc import aoc


def move(item, sequence):
    number, _ = item
    if number == 0:
        return sequence
    index = sequence.index(item)
    newseq = list(sequence)
    newseq.remove(item)
    newindex = (index + number) % (len(sequence) - 1)
    newseq.insert(newindex, item)
    return newseq


def mix(seq):
    for i in seq:
        seq = move(i, seq)
    return seq


def find_zero(seq):
    for i in range(len(seq)):
        if seq[i][0] == 0:
            return i


def get_coords(seq):
    start = find_zero(seq)
    vals = [seq[(start + offset) % len(seq)][0] for offset in (1000, 2000, 3000)]
    return sum(vals)


def mix2(seq, order):
    for i in order:
        seq = move(i, seq)
    return seq


def part1(values):
    decoded = mix(values)
    result = get_coords(decoded)
    assert result == 3 or result == 9866
    return


def part2(values):
    original = [(i * 811589153, position) for i, position in values]
    seq = list(original)
    for i in range(10):
        seq = mix2(seq, original)
    result = get_coords(seq)
    assert result == 1623178306 or result == 12374299815791
    return result


def run(file):
    data = aoc.loadlines(file)
    print("Part 1")
    values = [(int(number), position) for position, number in enumerate(data)]
    print(part1(values))
    print("Part 2")
    print(part2(values))


if __name__ == "__main__":
    print("Test Data")
    run("test.txt")
    print("Actual Data")
    run("data.txt")
    exit()
