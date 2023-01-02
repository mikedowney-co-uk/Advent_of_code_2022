from aoc import aoc
import numpy as np
from collections import deque

marker = 99  # flag exterior blocks


class Lava:
    def __init__(self, voxels):
        self.cube_min, self.cube_max = np.min(voxels), np.max(voxels) + 2
        self.space = np.zeros([self.cube_max, self.cube_max, self.cube_max])
        self.voxels = voxels
        for v in voxels:
            x, y, z = v
            self.space[x, y, z] = 1

    def out_of_bounds(self, x, y, z):
        return x < 0 or y < 0 or z < 0 or x >= self.cube_max or y >= self.cube_max or z >= self.cube_max

    def get_pixel(self, x, y, z):
        return 0 if self.out_of_bounds(x, y, z) else self.space[x, y, z]

    def count_neighbours(self, xyz):
        x, y, z = xyz
        return sum([self.get_pixel(x + 1, y, z), self.get_pixel(x - 1, y, z),
                    self.get_pixel(x, y + 1, z), self.get_pixel(x, y - 1, z),
                    self.get_pixel(x, y, z + 1), self.get_pixel(x, y, z - 1)])

    def measure_surface(self):
        surface = len(self.voxels) * 6
        for v in self.voxels:
            surface -= self.count_neighbours(v)
        return surface

    def is_pixel_outside(self, x, y, z):
        return 1 if self.out_of_bounds(x, y, z) or self.space[x, y, z] == marker else 0

    def count_edges(self, xyz):
        x, y, z = xyz
        return sum([self.is_pixel_outside(x + 1, y, z), self.is_pixel_outside(x - 1, y, z),
                    self.is_pixel_outside(x, y + 1, z), self.is_pixel_outside(x, y - 1, z),
                    self.is_pixel_outside(x, y, z + 1), self.is_pixel_outside(x, y, z - 1)
                    ])

    def add_if_empty(self, stack, xyz, direction):
        x, y, z = xyz
        xd, yd, zd = direction
        x += xd
        y += yd
        z += zd
        if not self.out_of_bounds(x, y, z) and self.space[x, y, z] == 0:
            stack.append((x, y, z))
            self.space[x, y, z] = marker

    def fill_from_point(self, start):
        stack = deque()
        self.add_if_empty(stack, start, (0, 0, 0))
        while stack:
            # print(len(stack))
            xyz = stack.pop()
            self.add_if_empty(stack, xyz, (1, 0, 0))
            self.add_if_empty(stack, xyz, (-1, 0, 0))
            self.add_if_empty(stack, xyz, (0, 1, 0))
            self.add_if_empty(stack, xyz, (0, -1, 0))
            self.add_if_empty(stack, xyz, (0, 0, 1))
            self.add_if_empty(stack, xyz, (0, 0, -1))

    def measure_outside(self):
        return sum([self.count_edges(v) for v in self.voxels])


def part1(world):
    surface = world.measure_surface()
    assert surface == 64 or surface == 4444
    return surface


def part2(world):
    all_edges = world.measure_surface()
    world.fill_from_point((0, 0, 0))
    surface = world.measure_outside()
    assert surface == 58 or surface == 2530
    return surface


def run(file):
    data = aoc.loadlines(file)
    voxels = aoc.parse_csv_int(data)
    space = Lava(voxels)
    print("Part 1")
    print(part1(space))
    print("Part 2")
    print(part2(space))


if __name__ == "__main__":
    print("Test Data")
    run("test.txt")
    print("Actual Data")
    run("data.txt")
    exit()
