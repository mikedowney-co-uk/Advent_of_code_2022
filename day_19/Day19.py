from aoc import aoc
from collections import deque
from time import perf_counter

O = "ore"
C = "clay"
OB = "obsidian"
G = "geode"

blueprints = []
blueprint = 0


class Robot:
    def __init__(self, makes, ore, clay=0, obsidian=0):
        """What it makes, and what's needed to make it"""
        self.makes = makes
        self.needs = {O: ore, C: clay, OB: obsidian}


def parse_line(line):
    print(line)
    numbers = aoc.extractints(line)
    ore = Robot(O, numbers[1])
    clay = Robot(C, numbers[2])
    obsidian = Robot(OB, numbers[3], clay=numbers[4])
    geode = Robot(G, numbers[5], obsidian=numbers[6])
    return {O: ore, C: clay, OB: obsidian, G: geode}


def build_blueprints(data):
    for line in data:
        robots = parse_line(line)
        blueprints.append(robots)
    return blueprints


def canwemake(robot, have):
    need = blueprint[robot]
    for element, howmany in need.needs.items():
        if howmany > have.get(element, 0):
            return False
    return True


def time_passes(robots, have):
    for kind in (O, C, OB, G):
        have.add(kind, robots.get(kind, 0))


def make_robot(kind, have):
    need = blueprint[kind]
    for element, howmany in need.needs.items():
        have.remove(element, howmany)
    return kind


def what_can_we_make(have):
    wecanmake = []
    for r in (G, OB, C, O):
        if canwemake(r, have):
            wecanmake.append(r)
    return wecanmake


def follow_recipe(actions, maxtime):
    recipe = list(actions)
    used = []
    robots = aoc.CountingDict()
    robots.add(O)
    have = aoc.CountingDict()
    for i in range(maxtime):
        # Start of a minute: start making a robot if we want to. Remove raw materials from inventory.
        # Current robots harvest materials.
        # Finally, new robot is ready to add to list.
        if recipe and canwemake(recipe[0], have):
            used.append(recipe[0])
            new_robot = make_robot(recipe.pop(0), have)
        else:
            new_robot = None
        time_passes(robots, have)
        if new_robot is not None:
            robots.add(new_robot)
    return have, used, recipe, robots


def follow_tree(maxtime):
    stack = deque()
    results = {}
    stack.append([])
    stop = False
    while stack:
        recipe = stack.popleft()
        result, used, leftover, robots = follow_recipe(recipe, maxtime)
        geodes = result.get(G, 0)
        if geodes > 0 and geodes not in results:
            results[geodes] = used
            print(len(stack), geodes, used)
        if not stop and not leftover:
            canmake = what_can_we_make(result)
            # Changed this so we keep making lesser ones until we can make a better one, instead of waiting
            # on a better one once we have the potential but not yet the quantity.
            if len(stack) > 100000:
                canmake = canmake[:3]
            for robot in canmake:
                # Only try to make the most valuable robot types
                # Optimization suggestion from slack: Once we have sufficient of a resource to make one of each type of
                # robot, we won't need any more robots for that resource and can skip them.
                newlist = list(recipe)
                newlist.append(robot)
                stack.append(newlist)
            if len(stack) > 5000000:
                stop = True
                print("Maximum stack length reached")
        if stop and len(stack) < 1000:
            stop = False
            print("Restarting")
    if len(results) == 0:
        return 0
    highest = sorted(results.keys(), reverse=True)[0]
    return highest


def part1():
    global blueprint
    # Tree search. At each node, get a list of robots we might be able to build with what we have, and
    # add it to the stack. Stop a 'leg' when we have leftover robots in the recipe.
    start = perf_counter()
    scores = []
    bp = 1
    for blueprint in blueprints:
        highest = follow_tree(24)
        print(bp, highest)
        scores.append(bp * highest)
        bp += 1
    end = perf_counter()
    quality = sum(scores)
    print("quality=", quality)
    print("took:", end - start)
    assert quality == 33 or quality == 1262
    return


def part2():
    global blueprint
    scores = 1
    for blueprint in blueprints[:3]:
        # optimization suggested in slack - not implemented yet
        maxneeded = aoc.CountingDict()
        for kind in (O, C, OB):
            maxneeded[kind] = sum([blueprint[r].needs[kind] for r in (O, C, OB, G)])
        highest = follow_tree(32)
        print(highest)
        scores *= highest
    print(scores)
    assert scores == 56 * 62
    return


def run(file):
    global blueprints
    data = aoc.loadlines(file)
    blueprints = build_blueprints(data)
    print("Part 1")
    print(part1())
    # print("Part 2")
    # print(part2())


if __name__ == "__main__":
    # print("Test Data")
    # run("test.txt")
    print("Actual Data")
    run("data.txt")
    exit()

# Timings (on test data):
# PyPy 7.3.9 (python 3.7.13) : 117.7s (down to 84.6s after optimizing)
# CPython 3.10.0: 982s
# CPython 3.11: 664.2
