from dijkstra import Graph, DijkstraSPF
from aoc.terrain import Terrain


def build_graph(terrain):
    """Yes, I know this is probably cheating a bit using someone else's implementation..."""
    graph = Graph()
    for y in range(terrain.height):
        for x in range(terrain.width):
            node = (x, y)
            moves = terrain.get_moves(node)
            for move in moves:
                graph.add_edge(str(node), str(move), 1)
    return graph


def solve(graph, start, end):
    dijkstra = DijkstraSPF(graph, str(start))
    return dijkstra.get_distance(str(end))


def part1(terrain):
    graph = build_graph(terrain)
    result = solve(graph, terrain.start, terrain.end)
    assert result == 31 or result == 504
    return result


def part2(terrain):
    allstarts = terrain.find("a")
    graph = build_graph(terrain)
    results = [solve(graph, start, terrain.end) for start in allstarts]
    results.sort()
    result = results[0]
    assert result == 29 or result == 500
    return result


def run(file):
    terrain = Terrain(file)

    print("Part 1")
    print(part1(terrain))
    print("Part 2")
    print(part2(terrain))


if __name__ == "__main__":
    print("Test Data")
    run("test.txt")
    print("Actual Data")
    run("data.txt")
    exit()
