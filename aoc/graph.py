class Node:
    def __init__(self, name):
        self.name = name
        self.connections = {}

    def add_link(self, target, distance):
        self.connections[target] = distance


class Graph:
    def __init__(self):
        self.nodes = {}

    def add_edge(self, source, destination, distance=1):
        if destination not in self.nodes:
            self.nodes[destination] = Node(destination)
        if source not in self.nodes:
            origin = Node(source)
            self.nodes[source] = origin
        else:
            origin = self.nodes[source]
        origin.add_link(destination, distance)
