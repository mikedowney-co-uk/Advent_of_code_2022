from aoc.filetree import FileTree
from aoc import aoc


class Disk:
    def __init__(self, script):
        self.path = []
        self.root = FileTree(self.path, "")
        self.cnode = self.root
        self.sizes = {}
        self.parse(script)

    def cd(self, p):
        if p == "/":
            self.path = [""]
            self.cnode = self.root
            return
        if p == "..":
            self.path.pop()
            self.cnode = self.cnode.parent
            return
        self.path.append(p)
        self.cnode = self.cnode.getchild(p)
        return

    def parse(self, script):
        for line in script:
            bits = line.split(" ")
            if bits[0] == "$":
                if bits[1] == "cd":
                    self.cd(bits[2])
                    continue
                if bits[1] == "ls":
                    # read until the next command
                    continue
            sizeordir = int(bits[0]) if bits[0] != "dir" else 0
            newnode = FileTree(self.path, bits[1], sizeordir)
            self.cnode.addnode(newnode)

    def getsize(self, node):
        if node.size != 0:
            return node.size
        s = sum([self.getsize(n) for n in node.children.values()])
        self.sizes[node.path] = s
        return s

    def countem(self):
        return sum([self.sizes[d] for d in self.sizes if self.sizes[d] <= 100000])


def part1(disk):
    disk.getsize(disk.root)
    total = disk.countem()
    print(total)
    assert (total == 1432936 or total == 95437)
    return total


def part2(disk):
    unused = 70000000 - disk.sizes["/"]
    needtofree = 30000000 - unused
    availabledirs = list(filter(lambda x: x >= needtofree, disk.sizes.values()))
    availabledirs.sort()
    dirsize = availabledirs[0]
    assert (dirsize == 272298 or dirsize == 24933642)
    return dirsize


def run(file):
    data = aoc.loadlines(file)
    disk = Disk(data)

    print("Part 1")
    print(part1(disk))
    print("Part 2")
    print(part2(disk))


if __name__ == "__main__":
    print("Test Data")
    run("test.txt")
    print("Actual Data")
    run("data.txt")
