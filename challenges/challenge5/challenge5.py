import random
from graph_adt_list import *
from graph_reader import *


def test_eularian_cycle(g=None):
    """ Takes in an graph object.
        Checks if the graph's vertices all have an even number of neighbors.

        Returns a boolean:
            True if all vertices have an even degree (is Eularian)
            False if even one vertex has an odd number of neighbors.
    """

    if not g:
        return "Please input a graph."

    for v in g.vertices:
        if len(v.getNeighbors()) % 2:
            return False
    return True


if __name__ == "__main__":
    vertices, edges = readGraph("graph_data.txt")
    g = LLGraph(vertices)
    g.addEdges(edges)
    print("This graph is Eulerian: " + str(test_eularian_cycle(g)))
