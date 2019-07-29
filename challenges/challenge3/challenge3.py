"""Challenge 3

Update your Graph ADT code to do the following

Implement Recursive Depth-first search to determine if there is a path between two vertices in a directed graph.
Input: A file containing a directed graph, a from_vertex and a to_vertex.

python3 challenge_3.py graph_data.txt 1 5

D
1,2,3,4,5
(1,2)
(1,4)
(2,3)
(2,4)
(3,5)
(5,2)
Output: If there is a path between the vertices (T/F) and the vertices in that path.

There exists a path between vertex 1 and 5: TRUE
Vertices in the path: 1,2,3,5
"""

from graph_reader import *
from graph_adt_list import *


def find_path(graph, nodeA, nodeB):
    """Iterative DFS to find the path from nodeA to nodeB.
       Returns an array of index.ids starting from nodeA's id to nodeB's id.
       Returns error messages if nodeA or nodeB is not in the graph, if there is
       graph entered or if there is no path from nodeA to nodeB
    """

    def findVertexIndex(vertex_id):
        # vertex argument is a string that is the label or id of the vertex , NOT a linkedlist object
        # returns the vertices index in the graph if present
        # otherwise returns False
        for i, v in enumerate(graph.vertices):
            if int(v.id) == int(vertex_id):
                return i
        return -1 # -1 is equivalent to false in this context as indices are range from 0 to len(graph.vertices)-1


    #nodeA and nodeB are the same.
    if nodeA == nodeB:
        # check to see if the vertex has a path to itself
        for v in nodeA.getNeighbors():
            if v == nodeA.id:
                return [nodeA.id]
        return "The node_to and the node_from are the same node, but there is no self-pointing edges."

    # check to see if the nodes are in the graph.
    nodeA_index = findVertexIndex(nodeA.id)
    nodeB_index = findVertexIndex(nodeB.id)
    if not nodeA_index > -1:
        return nodeA.id + " not in graph."
    if not nodeB_index > -1:
        return nodeB.id + " not in graph."

    # intialize result array, stack, and checkedSet
    result = []
    stack = []
    checkedSet = set()

    # append the starting vertex to the stack to be iterated through and add it to the set of checked vertices
    stack.append(nodeA)
    checkedSet.add(nodeA)

    # while items exist in the stack
    while stack:

        # pop the top item added to the element as is customary with DFS.
        current = stack.pop()
        # add the item's id to the result.
        result.append(current.id)

        # getNeighbors returns an array of vertex ids to look up...
        for vertex in current.getNeighbors():

            # look up the index into graph.vertices array based on the vertex's id.
            index = findVertexIndex(vertex)

            # if the item has an index of 0 or greater.
            # check to see if the linkedlist object at
            # that index in the graph.vertices array is the target (nodeB).
            if index > -1:
                if graph.vertices[index] == nodeB:
                    result.append(graph.vertices[index].id)
                    return result
                elif graph.vertices[index] not in checkedSet:
                    stack.append(graph.vertices[index])
                    checkedSet.add(graph.vertices[index])
            else:
                return str(vertex) + " is not in the graph."
    else:
        return "There is no path from "+ nodeA.id +" to " + nodeB.id +"."

    return "Empty graph." # the program should not run this code.



def recursive_DFS(graph, nodeA, nodeB):
        def findVertexIndex(vertex_id):
            # vertex argument is a string that is the label or id of the vertex , NOT a linkedlist object
            # returns the vertices index in the graph if present
            # otherwise returns False
            for i, v in enumerate(graph.vertices):
                if int(v.id) == int(vertex_id):
                    return i
            return -1 # -1 is equivalent to false in this context as indices are range from 0 to len(graph.vertices)-1

        def __helper_recursive_DFS(stack,result,checkedSet):
            # while items exist in the stack
            if stack:
                # pop the top item added to the element as is customary with DFS.
                current = stack.pop()
                # add the item's id to the result.
                result.append(current.id)

                # getNeighbors returns an array of vertex ids to look up...
                for vertex in current.getNeighbors():

                    # look up the index into graph.vertices array based on the vertex's id.
                    index = findVertexIndex(vertex)

                    # if the item has an index of 0 or greater.
                    # check to see if the linkedlist object at
                    # that index in the graph.vertices array is the target (nodeB).
                    if index > -1:
                        if graph.vertices[index] == nodeB:
                            result.append(graph.vertices[index].id)
                            return result
                        elif graph.vertices[index] not in checkedSet:
                            stack.append(graph.vertices[index])
                            checkedSet.add(graph.vertices[index])
                    else:
                        return vertex.id + " is not in the graph." # the program should not run this code.
            else:
                return "There is no path from "+ nodeA.id +" to " + nodeB.id +"."

            return __helper_recursive_DFS(stack,result,checkedSet)


        #nodeA and nodeB are the same.
        if nodeA == nodeB:
            # check to see if the vertex has a path to itself
            for v in nodeA.getNeighbors():
                if str(v) == nodeA.id:
                    return [nodeA.id]
            return "The node_to and the node_from are the same node, but there is no self-pointing edges."

        # check to see if the nodes are in the graph.
        nodeA_index = findVertexIndex(nodeA.id)
        nodeB_index = findVertexIndex(nodeB.id)
        if not nodeA_index > -1:
            return nodeA.id + " not in graph."
        if not nodeB_index > -1:
            return nodeB.id + " not in graph."
        # intialize result array, stack, and checkedSet
        result = []
        stack = []
        checkedSet = set()
        # append the starting vertex to the stack to be iterated through and add it to the set of checked vertices
        stack.append(nodeA)
        checkedSet.add(nodeA)

        return __helper_recursive_DFS(stack,result,checkedSet)


if __name__ == "__main__":
    filePath = sys.argv[1]
    from_vert = int(sys.argv[2])
    to_vert = int(sys.argv[3])

    data = readGraph(filePath)
    graph = LLGraph(data[0])
    graph.addEdges(data[1])

    nodeA = None
    nodeB = None

    for v in graph.vertices:
        if v.id == str(from_vert):
            nodeA = v
        if v.id == str(to_vert):
            nodeB = v

    if nodeA == None:
        print(str(from_vert) + " not in graph.")
    if nodeB == None:
        print(str(to_vert) + " not in graph.")

    if nodeA and nodeB:
        print(recursive_DFS(graph, nodeA, nodeB))
