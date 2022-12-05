from aoc import aoc
import re


def remove_char(stacks, chars_to_remove=1):
    """traverse down each stack and remove+discard the leftmost item"""
    return [s[chars_to_remove:] for s in stacks]


def get_leftmost_stack(stacks):
    return [s[0] for s in stacks if s[0] != " "]


def build_stacks(stacks):
    cratestacks = []
    while len(stacks[-1]) > 0:
        stacks = remove_char(stacks)
        cratestacks.append(get_leftmost_stack(stacks))
        stacks = remove_char(stacks, 3)
    return cratestacks


def move_one(cratestacks, wherefrom, whereto):
    crate = cratestacks[wherefrom-1].pop(0)
    newstack = [crate]
    newstack.extend(cratestacks[whereto-1])
    cratestacks[whereto-1] = newstack


def part1(stacks, moves):
    cratestacks = build_stacks(stacks)
    instructions = [[int(i) for i in re.findall("\\d+", m)] for m in moves]

    for no, wherefrom, whereto in instructions:
        for i in range(no):
            move_one(cratestacks, wherefrom, whereto)

    return "".join([c[0] for c in cratestacks])


def move_many(cratestacks, wherefrom, whereto, howmany):
    newstack = cratestacks[wherefrom-1][:howmany]
    cratestacks[wherefrom-1] = cratestacks[wherefrom-1][howmany:]
    newstack.extend(cratestacks[whereto-1])
    cratestacks[whereto-1] = newstack


def part2(stacks, moves):
    cratestacks = build_stacks(stacks)
    instructions = [[int(i) for i in re.findall("\\d+", m)] for m in moves]
    for no, wherefrom, whereto in instructions:
        move_many(cratestacks, wherefrom, whereto, no)
    return "".join([c[0] for c in cratestacks])


def run(file):
    print("Part 1")
    data = aoc.loadlines(file)
    stacks, moves = aoc.read_to_blank_line(data)
    print(part1(stacks, moves))
    print("Part 2")
    data = aoc.loadlines(file)
    stacks, moves = aoc.read_to_blank_line(data)
    print(part2(stacks, moves))


if __name__ == "__main__":
    print("Test Data")
    run("test.txt")
    print("Actual Data")
    run("data.txt")
