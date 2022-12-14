from functools import reduce
from operator import mul

from aoc import aoc


class Monkey:
    counter = 0
    factors = None

    def __init__(self):
        self.monkey = Monkey.counter
        self.items = []
        self.add = 0
        self.mul = 1
        self.power = 1
        self.test = None
        self.true = None
        self.false = None
        self.inspected = 0
        Monkey.counter += 1

    def worry(self):
        if self.power > 1:
            level = self.items[0] ** self.power
        else:
            level = ((self.items[0] + self.add) * self.mul)
        self.items[0] = int(level)
        self.inspected += 1
        return level

    def dotest(self):
        level = self.items[0]
        #         print(f"Monkey {self.monkey} testing {level}")
        return self.true if (level % self.test) == 0 else self.false

    def throw(self):
        return self.items.pop(0)

    def catch(self, item):
        self.items.append(item)

    def phew(self):
        self.items[0] = self.items[0] // 3

    def __str__(self):
        return f"Monkey:{self.monkey}, items: {self.items}, + {self.add} * {self.mul} ^ {self.power}, " + \
            f"test: {self.test}, true: {self.true}, false: {self.false}, Inspected={self.inspected}"


def load_monkeys(file):
    data = aoc.loadlines(file)
    monkeys = []
    Monkey.counter = 0

    while len(data) > 0:
        monkey = Monkey()
        data.pop(0)  # monkey number

        line = data.pop(0)  # starting items
        _, items = line.split(":")
        items = [int(i) for i in items.split(",")]
        monkey.items = items

        line = data.pop(0)  # operation
        op = line.split("= old ")[1]
        if "* old" in op:
            monkey.power = 2
        elif "*" in op:
            monkey.mul = int(op.split("*")[1])
        else:
            monkey.add = int(op.split("+")[1])

        line = data.pop(0)  # test
        monkey.test = int(line.split("by ")[1])

        line = data.pop(0)  # true
        monkey.true = int(line.split("monkey ")[1])

        line = data.pop(0)  # false
        monkey.false = int(line.split("monkey ")[1])

        monkeys.append(monkey)
        if len(data) > 0:
            data.pop(0)  # skip blank line

        # print(monkey)
    return monkeys


def action(monkey, monkeys):
    if len(monkey.items) == 0:
        return False
    #     print(monkey)
    monkey.worry()
    monkey.phew()
    throwto = monkey.dotest()
    item = monkey.throw()
    monkeys[throwto].catch(item)
    #     print(f"Throws {item} to {throwto}")
    return True


def business(monkeys, rounds):
    for r in range(rounds):
        for monkey in monkeys:
            while action(monkey, monkeys):
                pass
        # if r % 500 == 0:
        #     for m in monkeys:
        #         print(m)


def scores(monkeys):
    values = [monkey.inspected for monkey in monkeys]
    values.sort()
    return values[-1] * values[-2]


def part1(file):
    monkeys = load_monkeys(file)
    business(monkeys, 20)
    score = scores(monkeys)
    assert score == 10605 or score == 182293
    return score


def part2(file):
    monkeys = load_monkeys(file)

    factors = [m.test for m in monkeys]
    Monkey.factors = reduce(mul, factors, 1)

    def phew(self):
        self.items[0] = self.items[0] % Monkey.factors

    Monkey.phew = phew

    business(monkeys, 10000)
    score = scores(monkeys)
    assert score == 2713310158 or score == 54832778815
    return score


def run(file):
    print("Part 1")
    print(part1(file))
    print("Part 2")
    print(part2(file))


if __name__ == "__main__":
    # print("Test Data")
    # run("test.txt")
    print("Actual Data")
    run("data.txt")
    exit()
