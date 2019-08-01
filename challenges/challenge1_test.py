from challenge1 import *

filepath = "graph_data.txt"
data = read_graph(filepath)
assert data[0] == ['1', '2', '3', '4']
assert data[1] == [(1,2), (1,4), (2,3), (2,4)]

# linked list implementation
print("\ntesting linked list implementation...")
newGraph = LLGraph(data[0]) # adding the vertices
assert newGraph.numberOfVertices == 4
assert newGraph.get_vertices() == ['1', '2', '3', '4']

newGraph.add_edges(data[1]) # adding edges
assert newGraph.get_edges(1) == [(1, 2, 1), (1, 4, 1)]
assert newGraph.get_edges(2) == [(2, 3, 1), (2, 4, 1)]
assert newGraph.get_edges(3) and newGraph.get_edges(4) == "No out-going edges."

newGraph.add_edge(1, 3, 5)
assert newGraph.get_edges(1) == [(1, 2, 1), (1, 4, 1), (1, 3, 5)]
newGraph.add_edge(4, 3, 2)
assert newGraph.get_edges(4) == (4, 3, 2)
newGraph.add_edge(3, 4)
assert newGraph.get_edges(3) == (3, 4, 1)

assert newGraph.get_vertices() == ['1','2','3','4']
assert newGraph.numberOfVertices == 4
newGraph.add_vertex()
assert newGraph.get_vertices() == ['1','2','3','4','5']
assert newGraph.numberOfVertices == 5

assert newGraph.__iter__() == [['1', [(1, 2, 1), (1, 4, 1), (1, 3, 5)]], ['2', [(2, 3, 1), (2, 4, 1)]], ['3', (3, 4, 1)], ['4', (4, 3, 2)], ['5', 'No out-going edges.']]

assert newGraph.get_neighbors_of_a_vertex(1) == [2, 4, 3]

linkedL = LinkedList()
newGraph.vertices.append(linkedL)
newGraph.numberOfVertices += 1 # hacking my graph to test getVertex method
assert newGraph.get_vertex(newGraph.numberOfVertices) == linkedL

print("all linked-list-graph tests pass")

# adjacency matrix implementation
print("\ntesting adjacenecy matrix implementation...")
newGraph = AMGraph(len(data[0])) # adding the vertices
assert newGraph.numberOfVertices == 4
assert newGraph.vertices == [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
assert newGraph.get_vertices() == [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]

newGraph.add_edges(data[1]) # adding edges
assert newGraph.get_edges(1) == [0, 1, 0, 1]
assert newGraph.get_edges(2) == [0, 0, 1, 1]
assert newGraph.get_edges(3) and newGraph.get_edges(4) == [0, 0, 0, 0]

newGraph.add_edge(1, 3, 5)
assert newGraph.get_edges(1) == [0, 1, 5, 1]
newGraph.add_edge(4, 3, 2)
assert newGraph.get_edges(4) == [0, 0, 2, 0]
newGraph.add_edge(3, 4)
assert newGraph.get_edges(3) == [0, 0, 0, 1]

newGraph.add_vertex()
assert newGraph.numberOfVertices == 5
assert newGraph.vertices == [[0, 1, 5, 1, 0], [0, 0, 1, 1, 0], [0, 0, 0, 1, 0], [0, 0, 2, 0, 0], [0, 0, 0, 0, 0]]
assert newGraph.get_vertices() == [[0, 1, 5, 1, 0], [0, 0, 1, 1, 0], [0, 0, 0, 1, 0], [0, 0, 2, 0, 0], [0, 0, 0, 0, 0]]
print("all adjacenecy matrix graph tests pass")
