import sys


def readGraph(filepath):
    """input file should be of form:
        G
        1,2,3,4,5
        (1,2)
        (1,4)
        (2,3)
        (2,4)
        (2,5)
        (3,5)
    returns an array of vertices (ints) and and array of edges (tuple of two vertices: source to target)
    """

    edges = []
    listOfVertices = []
    graphType = ""

    with open(filepath, "r") as f:
        entries = f.read().split("\n")

    for i, entry in enumerate(entries):
        if i == 0: # the first entry is the type of the graph
            graphType = entry
        elif i == 1: # the second entry is a list of vertices
            listOfVertices = entry.split(",") # parse the string to get all numbers
        elif i > 1 and len(entry) > 0: # takes into account empty lines and lines not of the correct format
            entry = entry[1: len(entry)-1]
            entry = entry.split(",")
            if graphType == "G": # an undirected graph has "mirrored" edges
                edges.append((int(entry[0]), int(entry[1])))
                edges.append((int(entry[1]), int(entry[0])))
            else: # a directed graph has weighted edges, with a default weight of 1, if not input
                if len(entry) == 3:
                    edges.append((int(entry[0]), int(entry[1]), int(entry[2])))
                else:
                    edges.append((int(entry[0]), int(entry[1]), 1))

    return listOfVertices, edges
