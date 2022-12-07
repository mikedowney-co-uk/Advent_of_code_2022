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


class CountingDict(UserDict):
    """Counts how many times an item has been added, or sums the values added for a key"""

    def __setitem__(self, key, value):
        newvalue = value + self[key] if key in self else value
        super().__setitem__(key, newvalue)

    def add(self, key, value=1):
        self[key] = value


class FileTree():
    """Node is either a file,size for a directory"""

    def __init__(self, path, name, size=0):
        self.children = {}
        self.name = name
        self.size = size
        self.parent = self
        self.path = "/".join(path) + f"/{name}"

    def addnode(self, node):
        self.children[node.name] = node
        node.parent = self

    def getchild(self, name):
        return self.children[name]
