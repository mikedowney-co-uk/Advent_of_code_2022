class FileTree:
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
