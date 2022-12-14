from aoc import aoc
from time import perf_counter

air = "."
rock = "#"
sand = (500, 0)


class Cave:
    def __init__(self, data):
        self.walls = []
        self.left, self.right, self.top, self.bottom = 9999, -9999, 9999, -9999
        for line in data:
            corners = line.split(" -> ")
            coords = [[int(c) for c in corner.split(",")] for corner in corners]
            for c in coords:
                self.left = min(self.left, c[0])
                self.top = min(self.top, c[1])
                self.right = max(self.right, c[0])
                self.bottom = max(self.bottom, c[1])
            self.walls.append(coords)

        self.top = 0  # fix top in place
        self.width = self.right - self.left + 1
        self.height = self.bottom - self.top + 1

        self.grid = []

    def show(self):
        for row in self.grid:
            print(f" {row} ")

    def set_block(self, position, block):
        self.grid[position[1] - self.top][position[0] - self.left] = block

    def add_wall(self, start, end):
        begin = (min(start[0], end[0]), min(start[1], end[1]))
        finish = (max(start[0], end[0]), max(start[1], end[1]))
        for y in range(begin[1], finish[1] + 1):
            for x in range(begin[0], finish[0] + 1):
                self.set_block((x, y), rock)

    def build(self):
        self.grid = [[air] * self.width for _ in range(self.height)]
        for section in self.walls:
            start = section[0]
            for end in section[1:]:
                self.add_wall(start, end)
                start = end

    def get_move(self, position):
        """Returns the block the sand can move to, or a flag saying whether the block moved at all,
        with None if the block exits the grid."""
        starting_block = self.grid[position[1] - self.top][position[0] - self.left]
        if starting_block != air:
            return None
        for move in [(0, 1), (-1, 1), (1, 1)]:
            moveto = (position[0] + move[0], position[1] + move[1])
            try:  # This is faster than checking range first
                block = self.grid[moveto[1] - self.top][moveto[0] - self.left]
            except IndexError as ie:
                return None  # Fallen out of the world
            if block == air:
                return moveto
        # No moves left.
        return False

    def drop_sand(self, sand):
        moved = True
        while moved:
            moveto = self.get_move(sand)
            if moveto is None:
                return False
            if moveto is False:
                break
            sand = moveto
        self.set_block(sand, "o")
        return True


def fill_cave(cave, start):
    added = -1
    dropped = True
    while dropped:
        dropped = cave.drop_sand(start)
        added += 1
    return added


def part2(cave):
    # Extend the cave and add the floor
    cave.bottom += 2
    cave.height += 2
    cave.left -= cave.height
    cave.right += cave.height
    cave.width += 2 * cave.height
    cave.walls.append([[cave.left, cave.bottom], [cave.right, cave.bottom]])
    cave.build()
    added = fill_cave(cave, sand)
    print(added)
    assert added == 23921 or added == 93


def part1(cave):
    added = fill_cave(cave, sand)
    print(added)
    assert added == 24 or added == 763


def run(file):
    data = aoc.loadlines(file)
    cave = Cave(data)
    cave.build()
    # cave.show()
    print("Part 1")
    # part1(cave)

    print("Part 2")
    part2(cave)


if __name__ == "__main__":
    print("Test Data")
    run("test.txt")
    start = perf_counter()
    print("Actual Data")
    run("data.txt")
    end = perf_counter()
    print(end - start)
    exit()
