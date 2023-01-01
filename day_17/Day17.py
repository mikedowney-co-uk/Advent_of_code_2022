from aoc import aoc

winds = []
nwinds = 0
windcount = 0

width = 7

blocks = [
    ["####"],
    [" # ", "###", " # "],
    ["###", "  #", "  #"],
    ["#"] * 4,
    ["##"] * 2
]
background = " "


def get_gust():
    global windcount
    blow = winds[windcount]
    windcount = (windcount + 1) % nwinds
    return -1 if blow == "<" else 1


def isoverlap(grid, block, xy):
    block_x, block_y = xy
    block_h = len(block)
    block_w = len(block[0])
    for x in range(block_w):
        for y in range(block_h):
            if block[y][x] == "#" and grid[(block_y + y)][block_x + x] == "#":
                return True
    return False


def gridheight(grid):
    blankrow = background * width
    for y in range(len(grid)):
        if grid[y] == blankrow:
            return y
    return len(grid)


testgrid = [
    " " * width,
    " " * width,
    " " * width,
    " " * width,
    "      #",
    "     ##",
    "#" * width
]
testgrid.reverse()  # We need 0 at the bottom.

assert isoverlap(testgrid, blocks[0], (0, 0)) is True
assert isoverlap(testgrid, blocks[0], (3, 1)) is True
assert isoverlap(testgrid, blocks[0], (2, 2)) is False
assert gridheight(testgrid) == 3


# x is the left edge of the block
# y is the bottom of the block
def move_allowed(grid, block, xy, wind, gravity):
    """Returns 'Allowed','Resting'"""
    block_x, block_y = xy
    block_h = len(block)
    block_w = len(block[0])
    while block_y + block_h >= len(grid):
        grid.append(background * width)
    if block_x + wind < 0 or block_x + block_w + wind > width:
        return False, False
    if block_y - gravity < 0:
        return False, True

    new_x = block_x + wind
    new_y = block_y - gravity
    stuck = isoverlap(grid, block, (new_x, new_y))
    if not stuck:
        return True, False
    if stuck and gravity == 0:
        return False, False
    return False, True


assert move_allowed(testgrid, blocks[0], (2, 2), -1, 0) == (True, False)
assert move_allowed(testgrid, blocks[0], (2, 2), 1, 0) == (False, False)
assert move_allowed(testgrid, blocks[0], (2, 2), 0, 1) == (False, True)


def place_block(grid, block, xy):
    block_x, block_y = xy
    block_h = len(block)
    block_w = len(block[0])
    for x in range(block_w):
        for y in range(block_h):
            if block[y][x] == "#":
                grid[(block_y + y)] = aoc.insert(block[y][x], grid[(block_y + y)], block_x + x)


def drop_block(grid, block):
    x = 2
    y = gridheight(grid) + 3
    while True:
        wind = get_gust()
        canmove, resting = move_allowed(grid, block, (x, y), wind, 0)
        if canmove:
            x += wind
        canmove, resting = move_allowed(grid, block, (x, y), 0, 1)
        if canmove:
            y -= 1
        if resting:
            break
    place_block(grid, block, (x, y))


def show(grid):
    for y in range(1, len(grid) + 1):
        print(grid[-y])


def run_simulation(howmany):
    global windcount, background
    windcount = 0
    background = "."
    grid = [background * width] * 5
    # grid has ground level at 0

    for i in range(howmany):
        b = blocks[i % 5]
        drop_block(grid, b)
    return grid


def part1():
    grid = run_simulation(2022)
    height = gridheight(grid)
    assert height == 3068 or height == 3232
    return height


def find_repeats(grid, startat):
    rowsmatching = set(aoc.locate(grid, grid[startat]))
    for i in range(1, 10):
        indices = aoc.locate(grid, grid[startat + i])
        rowstokeep = set()
        for rowtocheck in indices:
            if rowtocheck - i in rowsmatching:
                rowstokeep.add(rowtocheck - i)
        rowsmatching = rowstokeep
    return rowsmatching


def search_for_repeats(grid):
    for s in range(len(grid) // 2):
        rows = find_repeats(grid, s)
        if len(rows) > 1:
            return rows


# Need to find out how often the pattern repeats so we can multiply them together to get the predicted height
# This is quite convoluted - there must be a much easier way of doing it but it's New Years Day and I'm tired
# and can't think of one at the moment.
def part2():
    global windcount
    windcount = 0

    # Get the grid heights where we see the repeats
    grid = run_simulation(10000)
    repeats = list(search_for_repeats(grid))
    repeats.sort()
    repeats_start_at = repeats[0]
    repeat_length = repeats[1] - repeats[0]

    # Now find out how many drops are needed to get these repeat heights
    grid = [background * width] * 5
    nextblock = 0
    windcount = 0
    drops = {}
    for i in range(repeat_length * 3):
        b = blocks[nextblock]
        nextblock = (nextblock + 1) % 5
        drop_block(grid, b)
        height = gridheight(grid)
        if (height - repeats_start_at) % repeat_length == 0:
            drops[height] = (i + 1)

    drops = list(drops.values())
    starts_repeating_after = drops[0]
    repeats_every = drops[1] - drops[0]
    number_of_drops = 1000000000000
    number_of_repeats = (number_of_drops - starts_repeating_after) / repeats_every
    tower_height = int(repeats_start_at + number_of_repeats * repeat_length)
    assert tower_height == 1514285714288 or tower_height == 1585632183915
    return tower_height


def run(file):
    global winds, nwinds
    data = aoc.load(file)
    winds = [a for a in data]
    nwinds = len(winds)

    print("Part 1")
    print(part1())
    print("Part 2")
    print(part2())


if __name__ == "__main__":
    print("Test Data")
    run("test.txt")
    print("Actual Data")
    run("data.txt")
    exit()
