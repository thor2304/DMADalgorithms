import string


class Graph:
    vertices = {}
    connections = None

    def __init__(self, number_of_nodes, connections):
        self.vertices = self.generate_vertices(number_of_nodes)
        self.connections = self.make_connections(connections)

    def generate_vertices(self, number_of_nodes):
        alphabet = string.ascii_lowercase
        nodes = {}
        for letter in range(number_of_nodes):
            nodes[alphabet[letter]] = self.Node(alphabet[letter])
        return nodes

    def make_connections(self, connections):
        for t in connections:
            n1 = self.vertices.get(t[0])
            n2 = self.vertices.get(t[1])
            n1.connect_node(n2)

    def __repr__(self):
        return str(self.vertices)

    class Node:
        visited = False
        connections = []
        name = ""
        discovery_time = None
        finishing_time = None

        def __init__(self, name):
            self.visited = False
            self.connections = []
            self.name = name

        def connect_node(self, node):
            """
            Adds a node to a list of connected nodes
            """
            self.connections.append(node)

        def get_connections(self):
            """
            Returns a list of connected nodes in alphabetic order based on their name
            """
            return sorted(self.connections, key=lambda x: x.name, reverse=False)

        def __repr__(self):
            return f"{[x.name for x in self.get_connections()]}"


class Kosaraju:
    vertices = None
    graph = None
    graph_transposed = None
    stack = []
    list_of_connections = []
    current_discovery_and_finishing_time = 1

    def __init__(self, number_of_nodes, connections):
        transposed_tuples = self.transpose_tuple(connections)
        self.number_of_nodes = number_of_nodes
        self.graph = Graph(number_of_nodes, connections)
        self.graph_transposed = Graph(number_of_nodes, transposed_tuples)
        self.generate_stack()
        self.find_components()
        self.print_result()

    def __repr__(self):
        return str(self.graph)
    def print_result(self):
        """
        Prints the result with the number of connections as well as the name
        of the nodes
        """
        print(f"There are {len(self.list_of_connections)} strongly coupled components:")
        for collection in self.list_of_connections:
            connection_string = "{"
            for node in collection:
                connection_string = connection_string + node.name + ", "
            connection_string = connection_string[:-2] + "}"
            print(connection_string)
        print()

    def find_components(self):
        """
        Pop nodes from the stack
        Perform DFS from the node.
        If list of connected nodes is empty or all of them have been visited
            Takes note of traversed nodes as being connected
        """
        while len(self.stack) > 0:
            node_name = self.stack.pop()
            node = self.graph_transposed.vertices.get(node_name.name)
            nodes_in_connection = self.DFS_connections(node, [])
            if len(nodes_in_connection) > 0:
                self.list_of_connections.append(nodes_in_connection)

    def generate_stack(self):
        """
        Performs a DFS.
        If a node has no unvisited node to go to and its not in the stack
        add it to the stack
        """
        listOfNodes = sorted(self.graph.vertices.values(),
                             key=lambda x: x.name, reverse=False)
        for node in listOfNodes:
            self.DFS_stackbuilder(node)

    def DFS_connections(self, node, nodes_in_connection):
        """
        Performs a DFS throughout the nodes in the graph.
        If the list of connected nodes is empty or if all of the nodes in the list
        have already been visited, add the node to the list of nodes in the connection.
        Returns a list of nodes in the connection
        """
        if node.visited == False:
            node.visited = True
            connections = node.get_connections()
            if len(connections) > 0:
                for connection in connections:
                    if connection.visited == False:
                        self.DFS_connections(connection, nodes_in_connection)
                        nodes_in_connection.append(node)
                    elif connection.visited == True and connection == connections[-1]:
                        if node not in nodes_in_connection:
                            nodes_in_connection.append(node)
            else:
                if node not in nodes_in_connection:
                    nodes_in_connection.append(node)

        return nodes_in_connection

    def DFS_stackbuilder(self, node):
        """
        Performs a DFS throughout the nodes in the graph.
        If the list of connected nodes is empty or if all of the nodes in the list
        have already been visited, add the node to the stack
        """
        if node.visited == False:
            node.visited = True
            node.discovery_time = self.current_discovery_and_finishing_time
            self.current_discovery_and_finishing_time += 1
            connections = node.get_connections()
            if len(connections) > 0:
                for connection in connections:
                    if connection.visited == False:
                        self.DFS_stackbuilder(connection)
                        self.addToStack(node)
                    if connection.visited == True and connection == connections[-1]:
                        self.setFinishingTime(node)
                        self.addToStack(node)
            else:
                self.setFinishingTime(node)
                self.addToStack(node)

    def transpose_tuple(self, connections):
        """
        Returns a list of transposed tuples.
        """
        transposed_connections = []
        for t in connections:
            transposed_connections.append((t[1], t[0]))
        return transposed_connections

    def addToStack(self, node):
        if node not in self.stack:
            self.stack.append(node)

    def setFinishingTime(self, node):
        node.finishing_time = self.current_discovery_and_finishing_time
        self.current_discovery_and_finishing_time += 1

    def print_discovery_time(self):
        for (key, value) in sorted(self.graph.vertices.items(), key= lambda x: x[1].discovery_time):
            print(key, " has discovery time", value.discovery_time)

    def print_finishing_time(self):
        for (key, value) in sorted(self.graph.vertices.items(), key= lambda x: x[1].finishing_time):
            print(key, " has finishing time", value.finishing_time)


connections = [
    ("a", "e"),
    ("a", "d"),
    ("a", "g"),

    ("b", "c"),

    ("c", "b"),

    ("d", "e"),

    ("f", "c"),
    ("f", "b"),
    ("f", "g"),

    ("g", "b"),
    ("g", "d"),
    ("g", "i"),
    ("g", "h"),

    ("h", "d"),
    ("h", "g"),
    ("h", "f"),

    ("i", "a"),
    ("i", "b"),
]

# Argument is the number of nodes
graph = Kosaraju(9, connections)
print(graph)
graph.print_discovery_time()
print()
graph.print_finishing_time()
