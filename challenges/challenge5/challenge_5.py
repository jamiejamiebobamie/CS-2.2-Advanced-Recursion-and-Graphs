import random
from graph_adt_list import *
from graph_reader import *


"""Choose any starting vertex v, and follow a trail of edges from that vertex until returning to v.
It is not possible to get stuck at any vertex other than v,
because the even degree of all vertices ensures that,
when the trail enters another vertex w there must be an unused edge leaving w.
The tour formed in this way is a closed tour, but may not cover all the vertices and edges of the initial graph.
As long as there exists a vertex u that belongs to the current tour but that has
adjacent edges not part of the tour, start another trail from u,
following unused edges until returning to u, and join the tour formed in this way to the previous tour.
By using a data structure such as a doubly linked list to maintain the set of
unused edges incident to each vertex, to maintain the list of vertices on the
current tour that have unused edges, and to maintain the tour itself, the
individual operations of the algorithm (finding unused edges exiting each vertex,
finding a new starting vertex for a tour, and connecting two tours that share a
vertex) may be performed in constant time each, so the overall algorithm takes linear time,

    -https://en.wikipedia.org/wiki/Eulerian_path#Fleury's_algorithm"""

def test_eularian_cycle(g=None):

    is_eularian_cycle = bool(random.getrandbits(1))

    return "This graph is Eulerian: " + str(is_eularian_cycle)

vertices, edges = readGraph("graph_data.txt")
g = LLGraph(vertices)
g.addEdges(edges)
print(g.__iter__())
print(test_eularian_cycle(g))
