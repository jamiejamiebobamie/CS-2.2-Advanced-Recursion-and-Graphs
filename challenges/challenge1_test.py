
import unittest
from challenge1 import *


class Test_Read_Graph_Method(unittest.TestCase):

    def __int__(self):
        self.filepath = "graph_data.txt"
        self.vertices, self.edges = read_graph(filepath)

    def test_read(self):
        self.assertTrue(self.vertices,['1', '2', '3', '4'])
        self.assertTrue(self.edges,[(1,2), (1,4), (2,3), (2,4)])


class Test_LLGraph_Methods(unittest.TestCase):

    def __init__(self):
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
        self.filepath = "graph_data.txt"
        self.vertices, self.edges = read_graph(filepath)
        self.LLGraph = LLGraph(le(self.vertices))

    def test_init__(self):
        self.assertTrue(self.LLGraph.numberOfVertices, 4)
        self.assertTrue(self.LLGraph.get_vertices(), [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]])

    def test_add_edges(self):
        self.LLGraph.add_edges(self.edges)
        self.assertTrue(self.LLGraph.get_edges(1), [0, 1, 0, 1])
        self.assertTrue(self.LLGraph.get_edges(2), [0, 0, 1, 1])
        self.assertTrue(self.LLGraph.get_edges(3), [0, 0, 0, 0])
        self.assertTrue(self.LLGraph.get_edges(4), [0, 0, 0, 0])
        self.LLGraph.add_edge(1, 3, 5)
        self.assertTrue(self.LLGraph.get_edges(1), [0, 1, 5, 1])
        self.LLGraph.add_edge(4, 3, 2)
        self.assertTrue(self.LLGraph.get_edges(4), [0, 0, 2, 0])
        self.LLGraph.add_edge(3, 4) # testing default weight of one if weight is not entered
        self.assertTrue(self.LLGraph.get_edges(3), [0, 0, 0, 1])

    def test_add_vertex(self):
        self.LLGraph.add_vertex()
        self.assertTrue(self.LLGraph.get_vertices(), [[0, 1, 5, 1, 0], [0, 0, 1, 1, 0], [0, 0, 0, 1, 0], [0, 0, 2, 0, 0], [0, 0, 0, 0, 0]])
        self.assertTrue(self.LLGraph.numberOfVertices, 5)

class Test_Dict_Graph_Methods(unittest.TestCase):

    def __init__(self):
        self.filepath = "graph_data.txt"
        self.vertices, self.edges = read_graph(filepath)
        self.LLGraph = LLGraph(self.vertices)

    def test_init__(self):
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

if __name__ == '__main__':
    unittest.main()
