import sys


class Graph:
    def __init__(self):
        self.vertices: dict[str, dict[str, int]] = {}

    def add_vertex(self, vertex: str) -> None:
        self.vertices[vertex] = {}

    def add_edge(self, start_vertex: str, end_vertex: str, cost: int) -> None:
        self.vertices[start_vertex][end_vertex] = cost

    def get_neighbors(self, vertex: str) -> dict[str, int]:
        return self.vertices[vertex]

    def dijkstra(self, start_vertex: str):
        distances: dict[str, int] = {v: sys.maxsize for v in self.vertices}
        distances[start_vertex] = 0
        visited = set()

        previous: dict[str, str] = {v: None for v in self.vertices}
        changed_edges: list[tuple[str, str]] = []
        visited_order: list[str] = []

        queue = [(start_vertex, 0)]
        while len(queue) > 0:
            queue = sorted(queue, key=lambda x: distances[x[0]])
            current_vertex, current_distance = queue[0]
            queue.remove((current_vertex, current_distance))
            if current_vertex in visited:
                continue

            visited.add(current_vertex)
            visited_order.append(current_vertex)

            for neighbor, cost_along_edge in self.get_neighbors(current_vertex).items():
                if current_distance + cost_along_edge < distances[neighbor]:
                    distances[neighbor] = current_distance + cost_along_edge
                    previous[neighbor] = current_vertex
                    changed_edges.append((current_vertex, neighbor))

                queue.append((neighbor, distances[neighbor]))

        return distances, previous, changed_edges, visited_order


def print_path_to_node(to: str, starting_at: str, previous_ordering: dict[str, str]):
    step = to
    backtrack = list(step)
    while step != starting_at and step is not None:
        step = previous_ordering[step]
        backtrack.append(step)

    print(list(reversed(backtrack)))


def print_all_paths(starting_at: str, graph: Graph, previous_ordering: dict[str, str]):
    for vertex in graph.vertices:
        print_path_to_node(vertex, starting_at, previous_ordering)


def main():
    # Example usage:
    graph = Graph()

    # Add vertexes
    graph.add_vertex('A')
    graph.add_vertex('B')
    graph.add_vertex('C')
    graph.add_vertex('D')
    graph.add_vertex('E')
    graph.add_vertex('F')
    graph.add_vertex('G')

    # Add edges with cost values
    graph.add_edge('A', 'B', 4)
    graph.add_edge('A', 'G', 7)

    graph.add_edge('B', 'C', 1)
    graph.add_edge('B', 'D', 2)

    graph.add_edge('C', 'A', 2)
    graph.add_edge('C', 'F', 6)

    graph.add_edge('D', 'C', 1)
    graph.add_edge('D', 'F', 4)

    graph.add_edge('E', 'C', 8)

    graph.add_edge('F', 'E', 1)

    graph.add_edge('G', 'E', 6)
    graph.add_edge('G', 'C', 4)

    start_vertex = 'A'
    distances, previous, changed_edges, visited_order = graph.dijkstra(start_vertex)

    print("Shortest distances from vertex", start_vertex + ":")
    for vertex, distance in distances.items():
        print(vertex, "-", distance)

    print("\nPrevious nodes:")
    for vertex, prev in previous.items():
        print(vertex, "-", prev)

    print("\nall paths:")
    print_all_paths(start_vertex, graph, previous)

    print("\nEdges changed by RELAX method:")
    for edge in changed_edges:
        print(edge[0], "->", edge[1])
    print(f"Total edges changed by RELAX: {len(changed_edges)}")

    print("\nVisited order:")
    print(visited_order)


if __name__ == '__main__':
    main()
