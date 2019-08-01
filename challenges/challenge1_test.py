
import unittest
from challenge1 import *


"""class Test_Read_Graph_Method(unittest.TestCase):

    def __init__(self):
        super(TestingClass, self).__init__()
        self.filepath = "graph_data.txt"
        self.vertices, self.edges = read_graph(filepath)

    def test_read(self):
        self.assertTrue(self.vertices,['1', '2', '3', '4'])
        self.assertTrue(self.edges,[(1,2), (1,4), (2,3), (2,4)])

class Test_LLGraph_Methods(unittest.TestCase):

    def __init__(self):
        super(TestingClass, self).__init__()
        self.filepath = "graph_data.txt"
        self.vertices, self.edges = read_graph(filepath)
        self.LLGraph = LLGraph(self.vertices)

    def test_init_(self):
        self.assertTrue(self.LLGraph.numberOfVertices, 4)
        self.assertTrue(self.LLGraph.get_vertices(), ['1', '2', '3', '4'])

    def test_add_edges(self):
        self.LLGraph.add_edges(self.edges)
        self.assertTrue(self.LLGraph.get_edges(1), [(1, 2, 1), (1, 4, 1)])
        self.assertTrue(self.LLGraph.get_edges(2), [(2, 3, 1), (2, 4, 1)])
        self.assertTrue(self.LLGraph.get_edges(3), "No out-going edges.")
        self.assertTrue(self.LLGraph.get_edges(4), "No out-going edges.")
        self.LLGraph.add_edge(1, 3, 5)
        self.assertTrue(self.LLGraph.get_edges(1), [(1, 2, 1), (1, 4, 1), (1, 3, 5)])
        self.LLGraph.add_edge(4, 3, 2)
        self.assertTrue(self.LLGraph.get_edges(4), (4, 3, 2))
        self.LLGraph.add_edge(3, 4) # testing default weight of one if weight is not entered
        self.assertTrue(self.LLGraph.get_edges(3), (3, 4, 1))

    def test_add_vertex(self):
        self.LLGraph.add_vertex()
        self.assertTrue(self.LLGraph.get_vertices(), ['1', '2', '3', '4', '5'])
        self.assertTrue(self.LLGraph.numberOfVertices, 5)

    # def test_iter_(self):
        # self.assertTrue(self.LLGraph.__iter__(), ['1', [(1, 2, 1), (1, 4, 1), (1, 3, 5)]], ['2', [(2, 3, 1), (2, 4, 1)]], ['3', (3, 4, 1)], ['4', (4, 3, 2)], ['5', 'No out-going edges.']])

    def test_get_neighbors_of_a_vertex(self):
        self.assertTrue(self.LLGraph.get_neighbors_of_a_vertex(1), [2, 4, 3])


class Test_AM_Graph_Methods(unittest.TestCase):

    def __init__(self):
        super(TestingClass, self).__init__()
        self.filepath = "graph_data.txt"
        self.vertices, self.edges = read_graph(filepath)
        self.AMGraph = AMGraph(len(self.vertices))

    def test_init_(self):
        self.assertTrue(self.AMGraph.numberOfVertices, 4)
        self.assertTrue(self.AMGraph.get_vertices(), [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]])

    def test_add_edges(self):
        self.AMGraph.add_edges(self.edges)
        self.assertTrue(self.AMGraph.get_edges(1), [0, 1, 0, 1])
        self.assertTrue(self.AMGraph.get_edges(2), [0, 0, 1, 1])
        self.assertTrue(self.AMGraph.get_edges(3), [0, 0, 0, 0])
        self.assertTrue(self.AMGraph.get_edges(4), [0, 0, 0, 0])
        selfAMLGraph.add_edge(1, 3, 5)
        self.assertTrue(self.AMGraph.get_edges(1), [0, 1, 5, 1])
        self.AMGraph.add_edge(4, 3, 2)
        self.assertTrue(self.AMGraph.get_edges(4), [0, 0, 2, 0])
        self.AMGraph.add_edge(3, 4) # testing default weight of one if weight is not entered
        self.assertTrue(self.AMGraph.get_edges(3), [0, 0, 0, 1])

    def test_add_vertex(self):
        self.AMGraph.add_vertex()
        self.assertTrue(self.AMGraph.get_vertices(), [[0, 1, 5, 1, 0], [0, 0, 1, 1, 0], [0, 0, 0, 1, 0], [0, 0, 2, 0, 0], [0, 0, 0, 0, 0]])
        self.assertTrue(self.AMGraph.numberOfVertices, 5)

class Test_Dict_Graph_Methods(unittest.TestCase):

    def __init__(self):
        super(TestingClass, self).__init__()
        self.filepath = "graph_data.txt"
        self.vertices, self.edges = read_graph(filepath)
        self.Graph = Graph(len(self.vertices))

    def test_init_(self):
        self.assertTrue(self.Graph.numberOfVertices, 4)
        self.assertTrue(self.Graph.get_vertices(), ['1', '2', '3', '4'])

    def test_add_edges(self):
        self.Graph.add_edges(self.edges)
        self.assertTrue(self.Graph.get_edges(1), [(1, 2, 1), (1, 4, 1)])
        self.assertTrue(self.Graph.get_edges(2), [(2, 3, 1), (2, 4, 1)])
        self.assertTrue(self.Graph.get_edges(3), "No out-going edges.")
        self.assertTrue(self.Graph.get_edges(4), "No out-going edges.")
        self.Graph.add_edge(1, 3, 5)
        self.assertTrue(self.Graph.get_edges(1), [(1, 2, 1), (1, 4, 1), (1, 3, 5)])
        self.Graph.add_edge(4, 3, 2)
        self.assertTrue(self.Graph.get_edges(4), (4, 3, 2))
        self.Graph.add_edge(3, 4) # testing default weight of one if weight is not entered
        self.assertTrue(self.Graph.get_edges(3), (3, 4, 1))

    def test_add_vertex(self):
        self.Graph.add_vertex()
        self.assertTrue(self.Graph.get_vertices(), ['1', '2', '3', '4', '5'])
        self.assertTrue(self.Graph.numberOfVertices, 5)

    # def test_iter_(self):
        # self.assertTrue(self.LLGraph.__iter__(), ['1', [(1, 2, 1), (1, 4, 1), (1, 3, 5)]], ['2', [(2, 3, 1), (2, 4, 1)]], ['3', (3, 4, 1)], ['4', (4, 3, 2)], ['5', 'No out-going edges.']])

    def test_get_neighbors_of_a_vertex(self):
        self.assertTrue(self.Graph.get_neighbors_of_a_vertex(1), [2, 4, 3])

if __name__ == '__main__':
    unittest.main()"""



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
