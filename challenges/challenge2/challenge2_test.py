from challenge2 import *

filepath = "graph_data.txt"


# print(data)
print('\ntesting readGraph function.')
data = readGraph(filepath)
assert data[0] == ['1', '2', '3', '4', '5']
assert data[1] == [(1, 2), (2, 1), (1, 4), (4, 1), (2, 3), (3, 2), (2, 4), (4, 2), (2, 5), (5, 2), (3, 5), (5, 3)]

print('\nreadGraph works. testing graph class initialization.')
new_graph = Graph(len(data[0]))

assert new_graph.numberOfVertices == 5
assert new_graph.vertices == [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]

print('\ngraph initialization works. testing addEdges and getVertices.')
new_graph.addEdges(data[1])
assert new_graph.getVertices() == [[0, 1, 0, 1, 0], [1, 0, 1, 1, 1], [0, 1, 0, 0, 1], [1, 1, 0, 0, 0], [0, 1, 1, 0, 0]]

print('\naddEdges and getVertices work. testing breadth_first_search.')
assert new_graph.breadth_first_search(filepath, 1, 3) == "Vertices in shortest path: 1,2,4,3\nNumber of edges in shortest path: 3"

print('\nbreadth_first_search works.\n\ntests complete. great job!')
