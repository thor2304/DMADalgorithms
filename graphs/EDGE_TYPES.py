from __future__ import annotations

time = 0
treeEdges = []
backEdges = []
forwardEdges = []
crossEdges = []


class Vertex:
    id: str = None
    connectedTo: dict[str, Vertex] = {}
    color: str = None
    d: int = None
    pi: Vertex | None = None
    f: float = None

    def __init__(self, key):
        self.id = key
        self.connectedTo: dict[str, Vertex] = {}
        self.color = "white"
        self.d = 0
        self.f = float("inf")
        self.pi = None

    def getNeighbors(self) -> dict[str, Vertex]:
        # self.connectedTo = OrderedDict(sorted(self.connectedTo.items()))
        return self.connectedTo

    def addNeighbor(self, nbr: Vertex) -> None:
        self.connectedTo[nbr.id] = nbr

    def __str__(self) -> str:
        return str(self.id) + ' connectedTo: ' + str([x for x in self.connectedTo])

    def __repr__(self) -> str:
        return self.__str__()


def add_neighbours(dict_in: dict[Vertex, list[Vertex]], sort_alphabetically: bool = True) -> None:
    for vertex, neighbours in dict_in.items():
        sorted_neighbours = sorted(neighbours, key=lambda x: x.id) if sort_alphabetically else neighbours
        for neighbour in sorted_neighbours:
            vertex.addNeighbor(neighbour)


def DFS_Visit(G: list[Vertex], u: Vertex) -> None:
    global time

    time = time + 1
    u.d = time
    u.color = "gray"
    for v in u.getNeighbors().values():
        if v.color == "white":
            v.pi = u
            DFS_Visit(G, v)

    u.color = "black"
    time = time + 1
    u.f = time


def DFS(G: list[Vertex]) -> None:
    global time

    for u in G:
        u.color = "white"
        u.pi = None
    time = 0
    for u in G:
        if u.color == "white":
            DFS_Visit(G, u)


def edge_check(G: list[Vertex]) -> None:
    global time

    for u in G:
        for v in u.getNeighbors().values():
            if v.pi == u:  # Note that tree edges are the edges that are explored by the parent
                treeEdges.append((u.id, v.id))

            # elif are needed to avoid double counting since we no longer have the time variable to help us
            elif v.d <= u.d < u.f <= v.f:
                backEdges.append((u.id, v.id))

            elif u.d < v.d < v.f < u.f:
                forwardEdges.append((u.id, v.id))

            elif v.d < v.f < u.d < u.f:
                crossEdges.append((u.id, v.id))

            else:
                print(f"Error on edge: ('{u.id}',  '{v}')")


def get_vertex_by_time_order(G: list[Vertex]) -> list[Vertex]:
    global time

    vertexs = []

    for i in range(time):
        for u in G:
            if (u.d == i):
                vertexs.append(u)
    return vertexs


def main():
    a = Vertex('a')
    b = Vertex('b')
    c = Vertex('c')
    d = Vertex('d')
    e = Vertex('e')
    f = Vertex('f')
    g = Vertex('g')
    h = Vertex('h')
    i = Vertex('i')

    add_neighbours({
        a: [d, b],
        b: [c, d],
        c: [e],
        d: [e],
        e: [b, f, g],
        f: [c, h, i],
        g: [d, h],
        h: [e, i],
        i: [],
    }, sort_alphabetically=True)

    Vertexs = [a, b, c, d, e, f, g, h, i]

    # s = Vertex('s')
    # z = Vertex('z')
    # y = Vertex('y')
    # w = Vertex('w')
    # x = Vertex('x')
    # v = Vertex('v')
    # t = Vertex('t')
    # u = Vertex('u')
    #
    # Vertexs = [s, z, y, w, x, v, t, u]
    #
    # add_neighbours({
    #     t: [v, u],
    #     u: [t, v],
    #     v: [s, w]
    # })

    DFS(Vertexs)

    edge_check(Vertexs)

    print("Tree Edges (" + str(len(treeEdges)) + "): ", treeEdges)
    print("Back Edges (" + str(len(backEdges)) + "): ", backEdges)
    print("Forward Edges (" + str(len(forwardEdges)) + "): ", forwardEdges)
    print("Cross Edges (" + str(len(crossEdges)) + "): ", crossEdges)

    for u in get_vertex_by_time_order(Vertexs):
        print(u.id, u.d, u.f)


if (__name__ == "__main__"):
    main()
