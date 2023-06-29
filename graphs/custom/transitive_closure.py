import networkx as nx

relations = [('a', 'b'), ('b', 'a'), ('b', 'b'), ('b', 'c')]

# Opret en orienteret graf
G = nx.DiGraph()

# Tilføj relationerne som kanter i grafen
G.add_edges_from(relations)

# Find den transitive lukning
transitive_closure = nx.transitive_closure(G)

# Udskriv de transitive relationer
output = list(transitive_closure.edges())
print(output)
print(len(output))
