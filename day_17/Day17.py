from aoc import aoc

winds = []
nwinds = 0
windcount = -1

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
    windcount += 1
    blow = winds[windcount % nwinds]
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


def part1(data):
    global background, windcount
    windcount = -1
    background = "."
    grid = [background * width] * 5
    # grid has ground level at 0

    for i in range(2022):
        b = blocks[i % 5]
        drop_block(grid, b)

    assert gridheight(grid) == 3068 or gridheight(grid) == 3232
    return gridheight(grid)


def part2(data):
    return


def run(file):
    global winds, nwinds
    data = aoc.load(file)
    winds = [a for a in data]
    nwinds = len(winds)

    print("Part 1")
    print(part1(data))
    print("Part 2")
    print(part2(data))


if __name__ == "__main__":
    print("Test Data")
    run("test.txt")
    print("Actual Data")
    run("data.txt")
    exit()
