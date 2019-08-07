import random
from graph_adt_list import *
from graph_reader import *


def test_eularian_cycle(edges=None):
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

    # No input
    if edges == None:
        return "Please input the edges from a graph to be tested."

    # initialize the return boolean
    is_eularian_cycle = True

    # create the edge_dictionary
    edge_dict = {}
    # iterate through the input edges
    for edge in edges:
    # check to see if the from_vert is in the dictionary
        if edge[0] not in edge_dict:
    # if it is, add the [to_vert] as the value of the entry
            edge_dict[edge[0]] = [edge[1]]
        else:
    # if it is append the new to_vert the from_vert's value array
            edge_dict[edge[0]].append(edge[1])
        if edge[1] not in edge_dict:
    # check to see if the to_vert is in the dictionary
            edge_dict[edge[1]] = [edge[0]]
        else:
    # if it is, add the [from_vert] as the value of the entry
            edge_dict[edge[1]].append(edge[0])

    print(edge_dict)

    # iterate through the items of the dictionaries
    # and check to see if any vertex has an odd degree.
    # if it does, retun False.
    for key,value in edge_dict.items():
    # as it is an undirected graph and we are adding the edges twice,
    # we'll never have an odd number of edges...
    # any integer times 2 == even... I'm confused.
        if len(value) != 1 and len(value) % 2 != 0:
            is_eularian_cycle = False

    return "This graph is Eulerian: " + str(is_eularian_cycle)

vertices, edges = readGraph("graph_data.txt")
g = LLGraph(vertices)
g.addEdges(edges)
print(g.__iter__())
print(test_eularian_cycle(edges))
