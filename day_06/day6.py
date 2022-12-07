from aoc import aoc


def aretheyunique(letters):
    s = set([l for l in letters])
    return len(s) == len(letters)


def get_marker(word, length=4):
    for i in range(len(word)):
        if aretheyunique(word[i:i + length]):
            return i + length  # skip 4 and report first char after 'start' marker


def part1(data):
    return get_marker(data)


def part2(data):
    return get_marker(data, 14)


def run(file):
    print("Part 1")
    data = aoc.load(file)
    print(part1(data))
    print("Part 2")
    print(part2(data))


if __name__ == "__main__":
    print("Test Data")
    run("test.txt")
    print("Actual Data")
    run("data.txt")
