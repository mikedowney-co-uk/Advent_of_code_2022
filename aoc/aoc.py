from collections import UserDict
import re


def load(filename, newline=True):
    """Loads a text file, adding a newline at the end if there isn't one
    or removing one if not required."""
    with open(filename) as f:
        text = f.read()
    if text[-1] != "\n" and newline:
        text += "\n"
    if text[-1] == "\n" and ~newline:
        return text[:-1]
    return text


def loadlines(filename, newline=True):
    return load(filename, newline).split("\n")


def read_to_blank_line(lines):
    output = []
    while len(lines) > 0:
        nextline = lines.pop(0)
        if nextline == "":
            break
        output.append(nextline)
    return output, lines


def parse_csv(data):
    return [[v for v in row.split(",")] for row in data]


def parse_csv_int(data):
    return [[int(v) for v in row.split(",")] for row in data]


intpattern = r"[+-]{0,1}\d+"


def extractints(s):
    return [int(i) for i in re.findall(intpattern, s)]


def sort_dict(d, reverse=False):
    """Returns keys for a dict, sorted"""
    return sorted(d, key=d.get, reverse=reverse)


def insert(char, string, where):
    return string[:where] + char + string[where + 1:]


assert insert("X", ".....", 2) == "..X.."
assert insert("X", ".....", 0) == "X...."
assert insert("X", ".....", 4) == "....X"


def locate(list_of_items, item_to_find):
    return [index for index, value in enumerate(list_of_items) if value == item_to_find]


def chebyshev(node1, node2):
    return max(abs(node1[0] - node2[0]), abs(node1[1] - node2[1]))


def compareint(left, right):
    if left == right:
        return 0
    else:
        return -1 if left < right else 1


class CountingDict(UserDict):
    """Counts how many times an item has been added, or sums the values added for a key"""

    def __setitem__(self, key, value):
        newvalue = value + self[key] if key in self else value
        super().__setitem__(key, newvalue)

    def add(self, key, value=1):
        self[key] = value

    def remove(self, key, value=1):
        newvalue = self[key] - value if key in self else -1
        if newvalue == 0:
            super().pop(key)
        elif newvalue > 0:
            super().__setitem__(key, newvalue)
        else:
            raise KeyError(f"Removing too many {key}, have {self[key]}, removing {value}")
