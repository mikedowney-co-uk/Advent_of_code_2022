import re
from aoc import aoc


class CaveWalk:
    def __init__(self, data):
        """Path has the caves visited, and valves opened, eg. AA,AA,BB is 'at cave AA', 'opened valve AA',
        'moved to cave BB'"""
        self.flows = {}
        self.exits = {}
        self.paths = {}
        self.parse(data)
        self.best = 0
        self.sortednodes = sorted(self.flows, key=self.flows.get, reverse=True)

    def parse(self, data):
        for row in data:
            valves = re.findall("[A-Z]{2}", row)
            flow = int(re.findall("\\d+", row)[0])
            valve = valves[0]
            pp = valves[1:]
            self.flows[valve] = flow
            self.exits[valve] = pp

## add a stop condition so it doesn't run forever.
    def walk(self, path, moveto, opened=None):
        if opened is None:
            opened = set()
        if len(path) == 30:
            value = self.pressure(path)
            self.paths[value] = path
            if value > self.best:
                self.best = value
                print(value, path)
            return
        current = "" if len(path) == 0 else path[-1]
        path.append(moveto)
        exits = self.exits[moveto]
        if not self.opened(moveto, opened):
            newset = set(opened)
            newset.add(moveto)
            self.walk(list(path), moveto, newset)  # open valve
        # try the highest value paths first

        for node in self.sortednodes:
            if node in exits and node != current:
                self.walk(list(path), node, opened)

    def opened(self, valve, opened):
        """Treat stuck valves as opened since we won't open them"""
        return self.flows[valve] == 0 or valve in opened

    def pressure(self, path):
        pressure = 0
        lastvisited = path[0]
        for time in range(len(path)):
            position = path[time]
            if position == lastvisited:
                pressure += self.flows[position] * (30 - time)
            lastvisited = position
        return pressure


testroute = ["AA", "DD", "DD", "CC", "BB", "BB", "AA", "II", "JJ", "JJ", "II", "AA", "DD", "EE", "FF", "GG", "HH",
             "HH", "GG", "FF", "EE", "EE", "DD", "CC", "CC"]
test = CaveWalk(aoc.loadlines("test.txt"))
assert test.flows["EE"] == 3
assert test.pressure(testroute) == 1651


def part1(data):
    cave = CaveWalk(data)
    cave.walk([], "AA")
    # for k, v in cave.paths.items():
    #     print(k, v)
    pressures = cave.paths.keys()
    print(pressures)
    best = sorted(pressures)[-1]
    print(best, cave.paths[best])
    assert best == 1651 or best == 1653
    return best


def part2(data):
    return


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
    exit()
