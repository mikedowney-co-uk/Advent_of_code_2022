from aoc import aoc


class Terrain:
    def __init__(self, file):
        data = aoc.loadlines(file)
        self.grid = [[l for l in line] for line in data]
        self.width, self.height = len(self.grid[0]), len(self.grid)
        self.start = self.find("S")[0]
        self.end = self.find("E")[0]

    def find(self, letter):
        matches = []
        for i, r in enumerate(self.grid):
            for j, c in enumerate(r):
                if c == letter:
                    matches.append((j, i,))
        return matches

    def outside(self, target):
        return target[0] < 0 or target[0] >= self.width or target[1] < 0 or target[1] >= self.height

    def get(self, position):
        return self.grid[position[1]][position[0]]

    def canwemove(self, origin, target):
        if self.outside(target):
            return False, None
        at = self.get(origin)
        if at == "S":
            at = "a"
        to = self.get(target)
        if to == "E":
            to = "z"
        return ord(to) <= (ord(at) + 1)

    def get_moves(self, position):
        """Return a list of possible moves"""
        moves = []
        for i, j in [(0, 1), (0, -1), (-1, 0), (1, 0)]:
            to = (position[0] + i, position[1] + j)
            if self.canwemove(position, to):
                moves.append(to)
        return moves
