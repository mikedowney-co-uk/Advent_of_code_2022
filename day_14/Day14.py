from aoc import aoc

air = "."
rock = "#"
sand = (500, 0)


class Cave:
    def __init__(self, data):
        self.walls = []
        self.left, self.right, self.top, self.bottom = [9999, -9999, 9999, -9999]
        for line in data:
            corners = line.split(" -> ")
            coords = [[int(c) for c in corner.split(",")] for corner in corners]
            for c in coords:
                self.left, self.top, self.right, self.bottom = \
                    [min(self.left, c[0]), min(self.top, c[1]), max(self.right, c[0]), max(self.bottom, c[1])]
            self.walls.append(coords)

        self.top = 0  # fix top in place
        self.width = self.right - self.left + 1
        self.height = self.bottom + 1

        self.grid = []

    def show(self):
        for row in self.grid:
            print(f" {row} ")

    def get_block(self, position):
        x = position[0] - self.left
        y = position[1] - self.top
        if x < 0 or x >= self.width or y >= self.height:  # Have we fallen off the play area?
            print("Left World at", x, y)
            return None
        row = self.grid[y]
        return row[x]

    def set_block(self, position, block):
        row = self.grid[position[1] - self.top]
        row = aoc.insert(block, row, position[0] - self.left)
        self.grid[position[1] - self.top] = row

    def add_wall(self, start, end):
        begin = [min(start[0], end[0]), min(start[1], end[1])]
        finish = [max(start[0], end[0]), max(start[1], end[1])]
        for y in range(begin[1], finish[1] + 1):
            for x in range(begin[0], finish[0] + 1):
                self.set_block((x, y), rock)

    def build(self):
        self.grid = [air * self.width for _ in range(self.height)]
        for section in self.walls:
            start = section[0]
            for end in section[1:]:
                self.add_wall(start, end)
                start = end

    def check_move(self, position, offset):
        block = self.get_block([position[0] + offset[0], position[1] + offset[1]])
        if block is None:
            return None
        return block == air

    def get_move(self, position):
        """Returns the block the sand can move to, followed by a flag saying whether the block moved at all.
        Returns None,False if the block exits the grid."""
        starting_block = self.get_block(position)
        if starting_block is None or starting_block != air:
            return None, False

        for move in [[0, 1], [-1, 1], [1, 1]]:
            canwe = self.check_move(position, move)
            if canwe is None:
                return None, False
            if canwe:
                moveto = (position[0] + move[0], position[1] + move[1])
                return moveto, True

        # No moves from left.
        return position, False

    def drop_sand(self, sand):
        moved = True
        while moved:
            moveto, moved = self.get_move(sand)
            if moveto is None:
                return False
            if moved:
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
    part1(cave)

    print("Part 2")
    part2(cave)


if __name__ == "__main__":
    print("Test Data")
    run("test.txt")
    print("Actual Data")
    run("data.txt")
    exit()
