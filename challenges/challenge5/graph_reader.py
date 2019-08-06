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
        elif i > 1 and len(entry) > 0 and len(entry) < 7: # takes into account empty lines and lines not of the correct format
            if graphType == "G": # an undirected graph has "mirrored" edges
                edges.append((int(entry[1]), int(entry[3])))
                edges.append((int(entry[3]), int(entry[1])))
            else:
                if len(entry) > 5:
                    edges.append((int(entry[1]), int(entry[3]), int(entry[5])))
                else:
                    edges.append((int(entry[1]), int(entry[3]), 1))

    return listOfVertices, edges
