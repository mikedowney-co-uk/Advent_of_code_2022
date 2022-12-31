import math

from aoc.graph import Node


def find_min_dist(queue: dict[str], dist: dict[str]) -> Node:
    sorted_nodes = sorted(queue, key=dist.get)
    return queue.pop(sorted_nodes[0])


class Dijkstra:
    def __init__(self, graph, start_node):
        self.graph = graph
        self.start_node = start_node

    def solve(self, target=None):
        # print(f"Solving for  {self.start_node} ->  {target}")
        queue = {}  # name:node
        dist = {}
        prev = {}
        for node in self.graph.nodes:
            dist[node] = math.inf
            queue[node] = self.graph.get_node(node)
        dist[self.start_node] = 0

        while queue:
            u = find_min_dist(queue, dist)
            for v in u.connections:
                alt = dist[u.name] + u.get_weight(v)
                if alt < dist[v]:
                    dist[v] = alt
                    prev[v] = u
            if u.name == target:
                return dist[u.name]
        return dist, prev
