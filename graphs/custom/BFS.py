from collections import OrderedDict

vertexAdded = []
vertexAddedStr = ""


class Vertex:
    id = None
    connectedTo = {}
    color = None
    d = None
    pi = None

    def __init__(self, key):
        self.id = key
        self.connectedTo = {}
        self.color = "white"
        self.d = 0
        self.pi = None

    def getNeighbors(self):
        self.connectedTo = OrderedDict(sorted(self.connectedTo.items()))
        return self.connectedTo

    def addNeighbor(self, nbr):
        self.connectedTo[nbr.id] = nbr

    def __str__(self):
        return str(self.id)


def add_neighbours(dict):
    for vertex, neighbours in dict.items():
        for neighbour in neighbours:
            vertex.addNeighbor(neighbour)


def BFS(G, s):
    for u in G:
        u.color = "white"
        u.d = float("inf")
        u.pi = None
    s.color = "gray"
    s.d = 0
    s.pi = None
    Q = []
    enqueue(Q, s)
    while Q != []:
        u = dequeue(G, Q)
        if u == None:
            return

        for v in u.getNeighbors().values():
            # print("Current Vertex: ", v.id)
            if v.color == "white":
                v.color = "gray"
                v.d = u.d + 1
                v.pi = u
                enqueue(Q, v)
        u.color = "black"


def enqueue(Q, u: Vertex):
    # print("Vertex to be added: ", u)
    addVertexToAddedList(u)
    if (u.id not in vertexAdded):
        Q.append(u.id)


def dequeue(G, Q):
    key = Q.pop(0)
    for i in range(len(G)):
        if G[i].id == key:
            # print("Vertex to be removed: ", G[i].id)
            return G[i]

    return None


def addVertexToAddedList(vertex: Vertex):
    global vertexAddedStr
    if (vertex not in vertexAdded):
        vertexAdded.append(vertex)
        vertexAddedStr += vertex.id
        # print("Vertex added: ", vertex.id)


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
    j = Vertex('j')

    add_neighbours({
        a: [g],
        b: [c, h],
        c: [a, h],
        d: [h, i, j],
        e: [b, d, f, h],
        f: [b, e],
        g: [c, j],
        h: [d, e, g, j],
        i: [d, h, i],
    })

    Vertexs = [a, b, c, d, e, f, g, h, i, j]

    BFS(Vertexs, a)

    print("Vertex Added order: ", vertexAddedStr)


if (__name__ == "__main__"):
    main()
