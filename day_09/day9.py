from aoc import aoc
import numpy as np
from scipy.spatial.distance import chebyshev


def move(direction, head, tail):
    """Takes a direction as a numpy array so (1,0) is one step right"""
    new = head + direction
    return new, movetail(new, tail)


def movetail(head, tail):
    difference = head - tail
    distance = chebyshev(head, tail)
    if distance > 1 and all(abs(difference) >= [1, 1]):
        tail = tail + np.sign(difference)
    elif distance > 1:
        tail = tail + np.ceil(difference / distance)
    return tail.astype(int)


def test():
    head = np.array([1, 3])
    tail = np.array([2, 4])
    right_step = np.array([1, 0])
    head, tail = move(right_step, head, tail)
    assert all(np.equal(tail, np.array([2, 4]))), "1"
    head, tail = move(right_step, head, tail)
    assert all(np.equal(tail, np.array([2, 4]))), '2'
    head, tail = move(right_step, head, tail)
    assert all(np.equal(tail, np.array([3, 3]))), "3"
    head, tail = move(right_step, head, tail)
    assert all(np.equal(tail, np.array([4, 3]))), "4"



moves = {
    "R": np.array([1, 0]),
    "L": np.array([-1, 0]),
    "U": np.array([0, 1]),
    "D": np.array([0, -1]),
}


def part1(data):
    head = np.array([0, 0])  # (x,y)
    tail = np.array([0, 0])

    visited = set()

    for line in data:
        angle, steps = line.split(" ")
        step = moves[angle]
        for i in range(int(steps)):
            head, tail = move(step, head, tail)
            visited.add(str(tail))
    print(len(visited))
    assert len(visited) == 6197 or len(visited) == 13


def part2(data):
    visited = set()
    rope = [np.array([0, 0])] * 10

    for line in data:
        angle, steps = line.split(" ")
        step = moves[angle]
        for _ in range(int(steps)):
            rope[0] = rope[0] + step  # move the head of the rope
            for j in range(1, 10):
                rope[j] = movetail(rope[j - 1], rope[j])
            visited.add(str(rope[-1]))

    assert len(visited) == 2562 or len(visited) == 36
    return len(visited)


def run(file):
    print("Part 1")
    data = aoc.loadlines(file)
    print(part1(data))
    print("Part 2")
    print(part2(data))


if __name__ == "__main__":
    test()
    print("Test Data 1")
    part1(aoc.loadlines("test1.txt"))
    part2(aoc.loadlines("test2.txt"))

    print("Actual Data")
    run("data.txt")

    exit()
