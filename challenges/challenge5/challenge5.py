import random
from graph_adt_list import *
from graph_reader import *


def test_eularian_cycle(g=None):
    """
       Problem:

        Determine if a given undirected graph is Eulerian (has an Eulerian Cycle).
        Euler's Theorem: A connected graph has an Euler cycle if every vertex has an even degree
        (an even number of edges extending from that vertex).

        Input: A file containing a undirected graph.

        Function:

        Takes in an array of edges (from_vert, to_vert) and creates a dictionary,
        then counts the number of values for each key.
        As the input edges are always from of an undirected graph
        (as per the problem's description),
        all edges are added to the dictionary twice like so:

        EDGE: (from_vert, to_vert)

        dict[from_vert] = to_vert
        dict[to_vert] = from_vert

        (ie each vert is both a key and a value)

        Finally iterate through the dictionaries items and check to see if any of the value arrays are odd numbered.
    """

    if g == None:
        return "Please input a graph."

    for v in g.vertices:
        if len(v.getNeighbors()) % 2:
            return False
    return True



    return "This graph is Eulerian: " + str(is_eularian_cycle)
