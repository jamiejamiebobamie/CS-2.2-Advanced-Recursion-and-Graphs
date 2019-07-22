from challenge1 import *

filepath = "graph_data.txt"
data = readGraph(filepath)
assert data[0] == ['1', '2', '3', '4']
assert data[1] == [(1,2), (1,4), (2,3), (2,4)]

# linked list implementation
print("linked list implementation")
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

# linked list implementation
print("linked list implementation")
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


# class AMGraph(object):
#     """An Graph ADT with adjacency matrix.
#     """
#     def __init__(self, numberOfVertices):
#         self.numberOfVertices = numberOfVertices
#         self.vertices = [[0]*self.numberOfVertices for _ in range(self.numberOfVertices)]
#
#     def addVertex(self, n=1):
#         """increases the number of vertices by n.
#         adds new edges of weight 0 to each of the existing vertices.
#         adds the new vertices to the end of the vertex matrix.
#         """
#         if n.isnumeric():   #   numbers wrapped in strings pass this check so...
#             number = int(n) #   cast the number to an int regardless.
#             self.numberOfVertices += number
#             for vertex in self.vertices:
#                 addVertices = [0]*number
#                 vertex.extend(addVertices)
#             self.vertices.append([0]*self.numberOfVertices)
#         else:
#             raise Exception("Please type a number.")
#
#     def addEdge(self,vFrom, vTo, weight=1):
#         """adds a directed edge from a vertex to a vertex with a given weight"""
#         # check to make sure the vertices exist:
#         if vFrom-1 >= 0 and vTo-1 >= 0 and vTo-1 <= self.numberOfVertices and vFrom-1 <= self.numberOfVertices:
#             self.vertices[vFrom-1][vTo-1] = weight
#
#     def addEdges(self, graph_data):
#         """takes in an array of tuples (from_vert, to_vert) and adds their edges of weight 1 to the graph."""
#         for entry in graph_data:
#             self.addEdge(entry[0],entry[1],1)
#
#     def getVertices(self):
#         """returns the vertex matrix"""
#         return self.vertices
#
#     def getEdges(self, vertex):
#         """returns the the edges for a single vertex"""
#         return self.vertices[vertex-1]
