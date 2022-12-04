from aoc import aoc


def priority(letter):
    asc = 1 + ord(letter) - ord("a")
    return asc if asc > 0 else 27 + ord(letter) - ord("A")


def halves(contents):
    return contents[:len(contents) // 2], contents[len(contents) // 2:]


def string2set(letters):
    s = set()
    for l in letters:
        s.add(l)
    return s


def sum_priorities(items):
    return sum([priority(item) for item in items])


def get_in_common(row):
    first, second = halves(row)
    return string2set(first).intersection(string2set(second))


def get_priority_for_common(row):
    return sum_priorities(get_in_common(row))


def part1(data):
    return sum([get_priority_for_common(datum) for datum in data])


def part2(data):
    priorities = 0
    for i in range(0, len(data), 3):
        elves = data[i:i+3]
        allhave = set(elves[0]) & set(elves[1]) & set(elves[2])
        priorities += priority(list(allhave)[0])
    return priorities


def run(file):
    print("Part 1")
    data = aoc.loadlines(file)
    print(part1(data))
    print("Part 2")
    print(part2(data))


if __name__ == "__main__":
    print("Test Data")
    run("test.txt")
    print("Actual Data")
    run("data.txt")
