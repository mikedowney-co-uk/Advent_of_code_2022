from aoc.dijkstra import Dijkstra
from aoc.graph import Graph
from aoc.terrain import Terrain


def build_graph(terrain, reverse=False):
    graph = Graph()
    for y in range(terrain.height):
        for x in range(terrain.width):
            node = (x, y)
            moves = terrain.get_moves(node)
            for move in moves:
                if reverse:
                    graph.add_edge(str(move), str(node), 1)
                else:
                    graph.add_edge(str(node), str(move), 1)
    return graph


def solve(graph, start, end=None):
    dijkstra = Dijkstra(graph, str(start))
    return dijkstra.solve(str(end))


def part1(terrain):
    graph = build_graph(terrain)
    result = solve(graph, terrain.start, terrain.end)
    assert result == 31 or result == 504
    return result


def part2(terrain):
    # Build the graph but with the directions pointing backwards
    allstarts = [str(a) for a in terrain.find("a")]
    graph = build_graph(terrain, reverse=True)
    results, _ = solve(graph, terrain.end)
    # Take the results where we ended up at one of the start positions
    has_correct_start = [r for r in results if r in allstarts]
    distances = [results[a] for a in has_correct_start]
    result = min(distances)
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
    print("Done.")
    exit()
