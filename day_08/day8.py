from aoc import aoc
import numpy as np
from time import perf_counter


class Forest:
    def __init__(self, grid):
        self.heights = np.array([[int(t) for t in row] for row in grid])
        self.height, self.width = len(grid), len(grid[0])

    def isvisible(self, x, y):
        if x == 0 or y == 0 or x == (self.width - 1) or y == (self.height - 1):
            return 1
        row = self.heights[y]
        tree = row[x]
        # This works because we're using numpy arrays not python lists.
        if all(row[:x] < tree) or all(row[x + 1:] < tree):
            return 1
        column = self.heights[:, x]
        if all(column[:y] < tree) or all(column[y + 1:] < tree):
            return 1
        return 0

    def scenic_score(self, x, y):
        row = self.heights[y]
        column = self.heights[:, x]
        tree = self.heights[y][x]
        return (
                count_in_dir(tree, row[x + 1:], 1) *
                count_in_dir(tree, row[:x], -1) *
                count_in_dir(tree, column[y + 1:], 1) *
                count_in_dir(tree, column[:y], -1)
        )

    def count(self):
        count = 0
        for y in range(self.height):
            for x in range(self.width):
                count += self.isvisible(x, y)
        return count

    def max_scenic(self):
        score = 0
        for y in range(self.height):
            for x in range(self.width):
                score = max(score, self.scenic_score(x, y))
        return score


def count_in_dir(tree, trees, direction):
    l = len(trees)
    if direction == 1:
        for i in range(l):
            if trees[i] >= tree:
                return 1 + i
    if direction == -1:
        for i in range(l):
            if trees[l - i - 1] >= tree:
                return i + 1
    return len(trees)


def part1(forest):
    count = forest.count()
    assert count == 21 or count == 1717
    return count


def part2(forest):
    score = forest.max_scenic()
    assert score == 8 or score == 321975
    return score


def run(file):
    print("Part 1")
    data = aoc.loadlines(file)
    forest = Forest(data)
    print(part1(forest))
    print("Part 2")
    print(part2(forest))


if __name__ == "__main__":
    start = perf_counter()
    print("Test Data")
    run("test.txt")
    print("Actual Data")
    run("data.txt")
    end = perf_counter()
    print(end - start)
