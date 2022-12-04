from aoc import aoc


def set_from_range(a, b):
    return set(range(a, b + 1))


def set_from_data(s):
    a, b = s.split("-")
    return set_from_range(int(a), int(b))


def get_jobs(row):
    elf1, elf2 = row.split(",")
    return set_from_data(elf1), set_from_data(elf2)


def one_is_subset(set1, set2):
    return set1.issubset(set2) or set2.issubset(set1)


def part1(data):
    count = 0
    for row in data:
        elf1, elf2 = get_jobs(row)
        count += 1 if one_is_subset(elf1, elf2) else 0
    return count


def part2(data):
    count = 0
    for row in data:
        elf1, elf2 = get_jobs(row)
        overlap = elf1 & elf2
        count += 1 if len(overlap) > 0 else 0
    return count


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
