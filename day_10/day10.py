from aoc import aoc


class CPU():
    def __init__(self, file):
        self.x = 1
        self.cycle = 1
        self.data = aoc.loadlines(file)
        self.strengths = {}

    def inc(self):
        if self.cycle % 20 == 0:
            self.strengths[self.cycle] = (self.x * self.cycle)
        self.cycle += 1

    def run(self):
        for instruction in self.data:
            self.execute(instruction)
        return self.strengths

    def execute(self, instruction):
        self.inc()
        if instruction == "noop":
            return
        self.inc()
        _, value = instruction.split(" ")
        self.x += int(value)


def part1(file):
    cpu = CPU(file)
    result = cpu.run()
    return sum([result[a] for a in [20, 60, 100, 140, 180, 220]])


class SPRITE(CPU):
    def __init__(self, file):
        super().__init__(file)
        self.display = []
        self.row = []

    def inc(self):
        pixel = (self.cycle - 1) % 40
        value = "#" if abs(pixel - self.x) <= 1 else " "
        self.row.append(value)
        if pixel == 39:
            self.display.append("".join(self.row))
            self.row = []
        self.cycle += 1


def part2(file):
    cpu = SPRITE(file)
    cpu.run()
    return cpu.display


def run(file):
    print("Part 1")
    print(part1(file))
    print("Part 2")
    for row in part2(file):
        print(row)


if __name__ == "__main__":
    print("Test Data")
    run("test.txt")
    print("Actual Data")
    run("data.txt")
    exit()
