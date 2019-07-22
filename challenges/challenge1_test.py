from challenge1 import *

filepath = "graph_data.txt"
data = readGraph(filepath)
assert data[0] == ['1', '2', '3', '4']
assert data[1] == [(1,2), (1,4), (2,3), (2,4)]

# linked list implementation
print("\ntesting linked list implementation...")
newGraph = LLGraph(data[0]) # adding the vertices
assert newGraph.numberOfVertices == 4
assert newGraph.getVertices() == ['1', '2', '3', '4']

newGraph.addEdges(data[1]) # adding edges
assert newGraph.getEdges(1) == [(1, 2, 1), (1, 4, 1)]
assert newGraph.getEdges(2) == [(2, 3, 1), (2, 4, 1)]
assert newGraph.getEdges(3) and newGraph.getEdges(4) == "No out-going edges."

newGraph.addEdge(1, 3, 5)
assert newGraph.getEdges(1) == [(1, 2, 1), (1, 4, 1), (1, 3, 5)]
newGraph.addEdge(4, 3, 2)
assert newGraph.getEdges(4) == (4, 3, 2)
newGraph.addEdge(3, 4)
assert newGraph.getEdges(3) == (3, 4, 1)

assert newGraph.getVertices() == ['1','2','3','4']
assert newGraph.numberOfVertices == 4
newGraph.addVertex()
assert newGraph.getVertices() == ['1','2','3','4','5']
assert newGraph.numberOfVertices == 5

assert newGraph.__iter__() == [['1', [(1, 2, 1), (1, 4, 1), (1, 3, 5)]], ['2', [(2, 3, 1), (2, 4, 1)]], ['3', (3, 4, 1)], ['4', (4, 3, 2)], ['5', 'No out-going edges.']]

assert newGraph.getNeighborsOfAVertex(1) == [2, 4, 3]

linkedL = LinkedList()
newGraph.vertices.append(linkedL)
newGraph.numberOfVertices += 1 # hacking my graph to test getVertex method
assert newGraph.getVertex(newGraph.numberOfVertices) == linkedL

print("all linked-list-graph tests pass")

# adjacency matrix implementation
print("\ntesting adjacenecy matrix implementation...")
newGraph = AMGraph(len(data[0])) # adding the vertices
assert newGraph.numberOfVertices == 4
assert newGraph.vertices == [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
assert newGraph.getVertices() == [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]

newGraph.addEdges(data[1]) # adding edges
assert newGraph.getEdges(1) == [0, 1, 0, 1]
assert newGraph.getEdges(2) == [0, 0, 1, 1]
assert newGraph.getEdges(3) and newGraph.getEdges(4) == [0, 0, 0, 0]

newGraph.addEdge(1, 3, 5)
assert newGraph.getEdges(1) == [0, 1, 5, 1]
newGraph.addEdge(4, 3, 2)
assert newGraph.getEdges(4) == [0, 0, 2, 0]
newGraph.addEdge(3, 4)
assert newGraph.getEdges(3) == [0, 0, 0, 1]

newGraph.addVertex()
assert newGraph.numberOfVertices == 5
assert newGraph.vertices == [[0, 1, 5, 1, 0], [0, 0, 1, 1, 0], [0, 0, 0, 1, 0], [0, 0, 2, 0, 0], [0, 0, 0, 0, 0]]
assert newGraph.getVertices() == [[0, 1, 5, 1, 0], [0, 0, 1, 1, 0], [0, 0, 0, 1, 0], [0, 0, 2, 0, 0], [0, 0, 0, 0, 0]]
print("all adjacenecy matrix graph tests pass")
