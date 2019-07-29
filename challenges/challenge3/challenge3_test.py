from graph_reader import *
from graph_adt_list import *
from challenge3 import *

filepath = "graph_data.txt"
filepath2 = "graph_data2.txt"
data = readGraph(filepath)
data2 = readGraph(filepath2)

# testing readGraph method
assert data[0] == ['1', '2', '3', '4', '5', '6']
assert data2[0] == ['6', '7', '8', '9', '10']
assert data[1] == [(1, 3, 1), (1, 2, 1), (2, 3, 1), (2, 4, 1), (3, 5, 1), (3, 3, 1), (4, 5, 1), (5, 2, 1), (5, 3, 1)]
assert data2[1] == [(6, 7, 1), (7, 7, 1), (8, 7, 1), (9, 7, 1), (7, 9, 1)]

new_graph = LLGraph(data[0])
new_graph.addEdges(data[1])

newer_graph = LLGraph(data2[0])
newer_graph.addEdges(data2[1])

assert new_graph.getEdges(1) == [(1, 3, 1), (1, 2, 1)]
assert newer_graph.getEdges(1) == (6, 7, 1)

# testing basic recursive_DFS functionality
assert recursive_DFS(new_graph, new_graph.vertices[0], new_graph.vertices[4]) == ['1', '2', '4', '5']
assert recursive_DFS(new_graph, new_graph.vertices[1], new_graph.vertices[4]) == ['2', '4', '5']
assert recursive_DFS(new_graph, new_graph.vertices[2], new_graph.vertices[4]) == ['3', '5']
assert recursive_DFS(new_graph, new_graph.vertices[3], new_graph.vertices[4]) == ['4', '5']
assert recursive_DFS(new_graph, new_graph.vertices[0], new_graph.vertices[3]) == ['1', '2', '4']
assert recursive_DFS(newer_graph, newer_graph.vertices[0], newer_graph.vertices[1]) == ['6', '7']

# testing if the input nodes are the same node
assert recursive_DFS(new_graph, new_graph.vertices[4], new_graph.vertices[4]) == "The node_to and the node_from are the same node, but there is no self-pointing edges."
assert recursive_DFS(newer_graph, newer_graph.vertices[1], newer_graph.vertices[1]) == ['7']

# testing if nodes are not in the graph
assert recursive_DFS(new_graph, newer_graph.vertices[1], new_graph.vertices[3]) == "7 not in graph."
assert recursive_DFS(new_graph, new_graph.vertices[1], newer_graph.vertices[3]) == "9 not in graph."
assert recursive_DFS(newer_graph, new_graph.vertices[1], new_graph.vertices[3]) == "2 not in graph."

# testing nodes where there is no path from the from_vert to the target node / to_vert
assert recursive_DFS(newer_graph, newer_graph.vertices[1], newer_graph.vertices[0]) == "There is no path from 7 to 6."
