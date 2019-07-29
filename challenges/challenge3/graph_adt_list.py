# The Graph Abstract Data Type (ADT) is defined as follows:
#
# class `Graph()``
# creates a new, empty graph.
#
# has the methods
# addVertex(vert) adds -> a new vertex
# addEdge(fromVert, toVert) adds -> a directed edge
# addEdge(fromVert, toVert, weight) adds -> a weighted, directed edge.
# getVertex(vertKey) finds -> the named vertKey
# getVertices() returns -> the list of all vertices.
#
# graph should be implemented with an adjacency list.


# NOTE:
#       I renamed this file graph_adt_list.py,
#       as opposed to the tutorial's suggested graph-adt-list.py
#       so that I could import it into other challenge files.

class LLGraph(object):
    """An Graph ADT with adjacency list.
    Graph -> LinkedList -> LinkedListNode(s)
    """
    def __init__(self, vertices=None):
        self.numberOfVertices = len(vertices)
        self.vertices = []
        for _ in range(self.numberOfVertices):
            new_LL = LinkedList(vertices[_])
            self.vertices.append(new_LL)

    def getVertex(self, n):
        """returns the associated LinkedList object if it exists."""
        return self.vertices[n-1] if n-1 < self.numberOfVertices and n > 0 else "Vertex index out of bounds. Please enter a vertex id between 1 and " + str(self.numberOfVertices) + "."

    def getVertices(self):
        """returns the id's/data of all the vertices in the graph"""
        result = []
        for v in self.vertices:
            result.append(v.id)
        return result

    def getNeighborsOfAVertex(self, vertex):
        """returns the id's/data of all of the neighbors of a given vertex."""
        if vertex > 0 and vertex-1 < self.numberOfVertices:
            return self.vertices[vertex-1].getNeighbors()

    def getEdges(self, vertex):
        """returns the the edges for a single vertex"""
        # print(vertex, self.vertices[vertex-1])
        return self.vertices[vertex-1].getEdges()

    def addEdge(self, f, t, cost=1):
        """add an edge from vertex f (a number) to vertex t (a number) with a default cost/weight of 1
        """
        if f-1 < self.numberOfVertices and f > 0:
            self.vertices[f-1].addNeighbor(t,cost)

    def addEdges(self, edgeData):
        """add the edges from an array of edge data.
        the array should look like:
        [
            ( from_vert, to_vert, optional_weight ) , ...
                                                            ]
        """
        for edge in edgeData:
            self.addEdge(*edge)

    def addVertex(self):
        """increases the number of vertices by one.
        adds a new edge of weight 0 to each of the existing vertices.
        adds the new vertex to the end of the vertex matrix.
        """
        self.numberOfVertices += 1
        new_linked_list = LinkedList(str(self.numberOfVertices))
        self.vertices.append(new_linked_list)

    def findVertexIndex(self, vertex_id):
        """vertex argument is a string that is the label or id of the vertex , NOT a linkedlist object
        returns the vertices index in the graph if present
        otherwise returns False
        admittedly this should be a method of the graph class...
        """
        for i, v in enumerate(self.vertices):
            if int(v.id) == int(vertex_id):
                return i
        return False


    def __iter__(self):
        """iterate over the vertex objects in the
        graph, to use sytax: for v in g
        """
        result = []
        for v in self.vertices:
            index = int(v.id)
            result.append([v.id, self.getEdges(index)])
        return result


class LinkedList(object):
    def __init__(self, vertex=None, head=None, tail=None):
        self.id = vertex # this is a string!
        self.length = 0
        self.head = head # the first vertex connected to the vertex at self.id.
        self.tail = tail

    def addNeighbor(self,data, weight=1):
        """Adds a single vertex to the linked list.
        """
        new_vertex = LinkedListNode(data, weight)
        if self.head == None:
            self.head = self.tail = new_vertex
        elif self.head == self.tail:
            self.tail = new_vertex
            self.head.next = new_vertex
        else:
            self.tail.next = new_vertex
            self.tail = new_vertex
        self.length += 1

    def getNeighbors(self):
        """Returns a list of all of the adjacent vertices' ids/data.
        """
        result = []
        node = self.head
        while node:
            result.append(node.data)
            node = node.next
        return result

    def getEdges(self):
        """Returns a list of all of the adjacent vertices in the form of:
            (current_vertex, target_vertex, weight of edge)
        """
        result = []
        node = self.head
        if node == None:
            return "No out-going edges."
        if self.head != self.tail:
            while node:
                result.append((int(self.id),node.data,node.weight))
                node = node.next
            else:
                return result
        else:
            return (int(self.id),node.data,node.weight)

class LinkedListNode(object):
    def __init__(self, data, weight=1):
        self.data = data
        self.weight = weight
        self.next = None
