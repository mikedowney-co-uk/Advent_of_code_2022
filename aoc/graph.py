import math


class Node:
    def __init__(self, name):
        self.name = name
        self.connections = {}

    def add_link(self, target, distance):
        self.connections[target] = distance

    def get_weight(self, node):
        return self.connections.get(node, math.inf)


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

    def get_node(self, node):
        return self.nodes[node]

    def get_connections(self, node):
        return self.nodes[node].connections

    def get_edge(self, node1, node2):
        return self.get_node(node1).get_weight(node2)
