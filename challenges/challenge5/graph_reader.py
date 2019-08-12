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
    returns an array of vertices (ints)
    and array of edges (tuple of two vertices: source to target)
    """

    edges = []
    listOfVertices = []
    graphType = ""

    with open(filepath, "r") as f:
        entries = f.read().split("\n")

    for i, entry in enumerate(entries):
        # the first entry is the type of the graph
        if i == 0:
            graphType = entry
        # the second entry is a list of vertices
        elif i == 1:
            # parse the string to get all numbers
            listOfVertices = entry.split(",")
        # takes into account empty lines
        elif i > 1 and len(entry) > 0:
            # an undirected graph has "mirrored" edges
            if graphType == "G":
                edges.append((int(entry[1]), int(entry[3])))
                edges.append((int(entry[3]), int(entry[1])))
            else:
                if len(entry) > 5:
                    edges.append((int(entry[1]), int(entry[3]), int(entry[5])))
                else:
                    edges.append((int(entry[1]), int(entry[3]), 1))

    return listOfVertices, edges
