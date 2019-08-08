from graph_reader import *
from graph_adt_list import *
from challenge5 import *

# testing a graph with vertices that have all even degrees.
vertices, edges = readGraph("graph_data.txt")
g = LLGraph(vertices)
g.addEdges(edges)
assert test_eularian_cycle(g) == True

# testing a graph with vertices that have all odd degrees.
vertices, edges = readGraph("graph_data1.txt")
g = LLGraph(vertices)
g.addEdges(edges)
assert test_eularian_cycle(g) == False

print("tests pass.")
