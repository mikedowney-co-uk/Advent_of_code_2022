from aoc import aoc


def calories_per_elf(rows):
    calories = 0
    maxcal = 0
    for row in rows:
        if len(row) == 0:
            maxcal = max(maxcal, calories)
            calories = 0
        else:
            c = int(row)
            calories += c
    print("Calories:", maxcal)


def calories_per_elf2(rows):
    elf = 1
    allcals = aoc.CountingDict()
    for row in rows:
        if len(row) == 0:
            elf += 1
        else:
            allcals[elf] = int(row)
    return allcals


def run(file):
    print("Part 1")
    test = aoc.loadlines(file)
    calories_per_elf(test)
    print("Part 2")
    c = calories_per_elf2(test)
    sorted_keys = aoc.sort_dict(c, True)
    print(sorted_keys[:3])


if __name__ == "__main__":
    print("Test Data")
    run("test.txt")
    print("Actual Data")
    run("data.txt")
