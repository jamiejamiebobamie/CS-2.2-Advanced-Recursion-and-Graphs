import sys # Library for INT_MAX

import random


from graph_reader import *
from graph_adt_list import *

# class Graph():
#
#     def __init__(self, vertices):
#         self.V = vertices
#         self.graph = [[0 for column in range(vertices)]
#                     for row in range(vertices)]
#
#     # A utility function to print the constructed MST stored in parent[]
#     def printMST(self, parent):
#         print "Edge \tWeight"
#         for i in range(1, self.V):
#             print parent[i], "-", i, "\t", self.graph[i][ parent[i] ]
#
#     # A utility function to find the vertex with
#     # minimum distance value, from the set of vertices
#     # not yet included in shortest path tree
#     def minKey(self, key, mstSet):
#
#         # Initilaize min value
#         min = sys.maxint
#
#         for v in range(self.V):
#             if key[v] < min and mstSet[v] == False:
#                 min = key[v]
#                 min_index = v
#
#         return min_index

    # Function to construct and print MST for a graph
    # represented using adjacency matrix representation
# def primMST(graph):
#
#     visited = []
#     unvisited = []
#
#     i = 1
#
#     for v in graph.vertices:
#         unvisited.append(v)                     # appending the linkedlist object
#
#     # choose a random index
#     index = random.randint(0, graph.numberOfVertices-i)
#
#     # print(index)
#
#     visited.append(unvisited.pop(index).id)
#
#     while unvisited:
#

#
#         edges = graph.vertices[index].getEdges()
#
#         lowest = float('inf')
#         lowest_vert = None
#
#         if isinstance(edges, list):                # if more than one edge..
#             for edge in edges:
#                 if edge[1] not in visited:
#                     temp = lowest
#                     lowest = min(edge[2], lowest)
#                     if temp != lowest:
#                         lowest_vert = edge[1]
#         else:                                       # if just one edge..
#             if edges[1] not in visited:
#                 temp = lowest
#                 lowest = min(edges[2], lowest)
#                 if temp != lowest:
#                     lowest_vert = edges[1]
#
#         for i, v in enumerate(unvisited):
#             if v.id == lowest_vert:
#                 visited.append(unvisited.pop(i).id)
#
#         i+=1
#
#     else:
#         return visited

def primMST(graph,edges):
    """If it's a digraph all vertices must be represented
    in both to_vert and from_vert positions in:
    [to_vert, from_vert, weight]
    """

    # choose a random index
    index = random.randint(0, graph.numberOfVertices-1)
    vertex = int(graph.vertices[index].id)

    MST = []
    visited = []
    minEdge = [None,None,float('inf')] # [to_vert, from_vert, weight]

    minEdge_index = 0

    # number of edges in a minimum spanning tree is graph.numberOfVertices-1
    while len(MST) < graph.numberOfVertices-1:

        visited.append(vertex) # append the new vertex to the visited array

        for i, edge in enumerate(edges):
            if edge[2] < minEdge[2] and edge[1] not in visited and edge[0] in visited and edge[0] != edge[1]:
                minEdge = edge
                minEdge_index = i

        edges.pop(minEdge_index)

        MST.append(minEdge)

        vertex = minEdge[1]
        minEdge = [None,None,float('inf')]

    return MST


if __name__ == "__main__":

    filePath = "graph_data.txt"
    vertices, edges = readGraph(filePath)

    graph = LLGraph(vertices)
    graph.addEdges(edges)

    print(primMST(graph, edges))
