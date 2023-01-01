from collections import UserDict


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


class CountingDict(UserDict):
    """Counts how many times an item has been added, or sums the values added for a key"""

    def __setitem__(self, key, value):
        newvalue = value + self[key] if key in self else value
        super().__setitem__(key, newvalue)

    def add(self, key, value=1):
        self[key] = value
