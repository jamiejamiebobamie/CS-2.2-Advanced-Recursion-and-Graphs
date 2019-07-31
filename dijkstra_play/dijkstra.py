

from graph_reader import *
from graph_adt_list import *

def dijkstra(graph):

    unvisited = []
    visited = []

    previous = {}
    shortest = {}

    for v in graph.vertices:
        unvisited.append(v.id)
        shortest[v.id] = float("inf")

    while unvisited:

        current = unvisited.pop()

        # if this is the starting vertex, intialize its shortest dictionary value to 0
        if len(unvisited) == graph.numberOfVertices - 1:
            shortest[current] = 0
            previous[current] = None

        for v in graph.vertices:
            if v.id == current:
                edges = v.getEdges()
                print(edges)
                if isinstance(edges, tuple):
                    # print(unvisited, shortest, edges)# edges[2] < shortest[edges[1]])
                    if str(edges[1]) not in visited:
                        if edges[2] < shortest[str(edges[1])]:
                            shortest[str(edges[1])] = edges[2]
                            previous[str(edges[1])] = edges[0]
                else:
                    for edge in edges:
                        print(edge[1])
                        if str(edge[1]) not in visited:
                            if edge[2] < shortest[str(edge[1])] and edge[1] != edge[0]:
                                shortest[str(edge[1])] = edge[2]
                                previous[str(edge[1])] = edge[0]

        visited.append(current)

    return shortest, previous



if __name__ == "__main__":
    filePath = "graph_data.txt"

    data = readGraph(filePath)
    graph = LLGraph(data[0])
    graph.addEdges(data[1])
    print(graph.__iter__())
    print(dijkstra(graph))
