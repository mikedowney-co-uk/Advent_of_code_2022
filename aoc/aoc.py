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


def read_to_blank_line(lines):
    output = []
    while len(lines) > 0:
        nextline = lines.pop(0)
        if nextline == "":
            break
        output.append(nextline)
    return output, lines


def sort_dict(d, reverse=False):
    """Returns keys for a dict, sorted"""
    return sorted(d, key=d.get, reverse=reverse)


class CountingDict(UserDict):
    """Counts how many times an item has been added, or sums the values added for a key"""

    def __setitem__(self, key, value):
        newvalue = value + self[key] if key in self else value
        super().__setitem__(key, newvalue)

    def add(self, key, value=1):
        self[key] = value


