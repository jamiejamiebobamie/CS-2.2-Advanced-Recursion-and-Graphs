import sys
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

        # I looked at Vincenzo's code for guidance
        # and implemented the edge case of there being no neighbors.
        # https://github.com/C3NZ/CS22/blob/
            # ded71687fc91aa6f6b5d7c7a86ffde7fb570d7c0/
                # challenges/graphs/graph.py#L358

        # I also double checked what was being returned by .getNeighbors()
            # which is an array of all the vertices
                # that are adjacent to a given vertex.

        # Example:
        # [2, 5]
        # [1, 3]
        # [2, 4]
        # [3, 5]
        # [4, 1]

        if len(v.getNeighbors()) % 2 != 0 or len(v.getNeighbors()) == 0 :
            return False
    return True


if __name__ == "__main__":

    file_path = sys.argv[1]

    if file_path:
        vertices, edges = readGraph(file_path)
    else:
        vertices, edges = readGraph("graph_data.txt")

    g = LLGraph(vertices)
    g.addEdges(edges)
    print("This graph is Eulerian: " + str(test_eularian_cycle(g)))
