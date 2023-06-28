from collections import defaultdict


# class to represent a graph object
class Graph:
    # Constructor
    def __init__(self, vertices):
        # A dictionary to represent an adjacency list
        self.adjList = defaultdict(list)
        # stores in-degree of a vertex
        # initialize in-degree of each vertex by 0
        self.indegree = defaultdict(int)
        # add vertices to the graph
        self.vertices = vertices
        # add edges to the graph
        for vertex in vertices:
            self.adjList[vertex] = []
            self.indegree[vertex] = 0

    # function to add an edge to the graph
    def addEdge(self, src, dest):
        self.adjList[src].append(dest)
        self.indegree[dest] += 1


# Recursive function to find all topological orderings of a given DAG
def findAllTopologicalOrders(graph, path, discovered, N):
    # do for every vertex
    for v in graph.vertices:
        # proceed only if in-degree of current node is 0 and current node is not processed yet
        if graph.indegree[v] == 0 and not discovered[v]:
            # for every adjacent vertex u of v, reduce in-degree of u by 1
            for u in graph.adjList[v]:
                graph.indegree[u] -= 1
            # include current node in the path and mark it as discovered
            path.append(v)
            discovered[v] = True
            # recur
            findAllTopologicalOrders(graph, path, discovered, N)
            # backtrack: reset in-degree information for the current node
            for u in graph.adjList[v]:
                graph.indegree[u] += 1
            # backtrack: remove current node from the path and mark it as undiscovered
            path.pop()
            discovered[v] = False
    # print the topological order if all vertices are included in the path
    if len(path) == N:
        print(path)


# Print all topological orderings of a given DAG
def printAllTopologicalOrders(graph):
    # get number of nodes in the graph
    N = len(graph.vertices)
    # create an auxiliary space to keep track of whether vertex is discovered
    discovered = defaultdict(bool)
    # list to store the topological order
    path = []
    # find all topological ordering and print them
    findAllTopologicalOrders(graph, path, discovered, N)


# Driver code
if __name__ == '__main__':
    # List of graph edges as per above diagram
    edges = [
        ('b', 'a'),
        ('b', 'd'),
        ('d', 'a'),
        ('b', 'c'),
        ('d', 'e'),
        ('b', 'e'),
        ('c', 'e'),
        ('f', 'c'),
        ('f', 'e')
    ]
    vertices = ['a', 'b', 'c', 'd', 'e', 'f']
    print("All Topological sorts")
    # create a graph from edges
    graph = Graph(vertices)
    # add edges to the graph
    for edge in edges:
        graph.addEdge(edge[0], edge[1])
    # print all topological orderings of the graph
    printAllTopologicalOrders(graph)