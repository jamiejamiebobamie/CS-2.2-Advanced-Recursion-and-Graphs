"""Challenge 1
- Implement the Graph ADT with an adjacency list
- Implement the Graph ADT with an adjacency matrix
- Implement code to read in a graph from a text file to create an instance of the Graph ADT and use it's methods.
- Test your code.


### Stretch Challenges 1
- Re-implement the Graph ADT with adjacency matrix using one of the
[python collections](https://docs.python.org/3.6/library/collections.html#module-collections)"""


def readGraph(filepath):
    """input file should be of form:
        1,2,3,4
        (1,2)
        (1,4)
        (2,3)
        (2,4)
    returns an array of vertices (ints) and and array of edges (tuple of two vertices: source to target)
    """
    edges = []
    listOfVertices = []

    with open(filepath, "r") as f:
        entries = f.read().split("\n")

    for i, entry in enumerate(entries):
        if i == 0: # the first entry is a list of vertices
            listOfVertices = entry.split(",")  # parse the string to get all numbers
        elif len(entry) > 0: # takes into account empty lines
            edges.append((int(entry[1]), int(entry[3]))) # this assumes the graph IS directed (a digraph)

    return listOfVertices, edges

class AMGraph(object):
    """An Graph ADT with adjacency matrix.
    """
    def __init__(self, numberOfVertices):
        self.numberOfVertices = numberOfVertices
        self.vertices = [[0]*self.numberOfVertices for _ in range(self.numberOfVertices)]

    def addVertex(self, n=1):
        """increases the number of vertices by n.
        adds new edges of weight 0 to each of the existing vertices.
        adds the new vertices to the end of the vertex matrix.
        """
        if n.isnumeric():   #   numbers wrapped in strings pass this check so...
            number = int(n) #   cast the number to an int regardless.
            self.numberOfVertices += number
            for vertex in self.vertices:
                addVertices = [0]*number
                vertex.extend(addVertices)
            self.vertices.append([0]*self.numberOfVertices)
        else:
            raise Exception("Please type a number.")

    def addEdge(self,vFrom, vTo, weight=1):
        """adds a directed edge from a vertex to a vertex with a given weight"""
        # check to make sure the vertices exist:
        if vFrom-1 >= 0 and vTo-1 >= 0 and vTo-1 <= self.numberOfVertices and vFrom-1 <= self.numberOfVertices:
            self.vertices[vFrom-1][vTo-1] = weight

    def addEdges(self, graph_data):
        """takes in an array of tuples (from_vert, to_vert) and adds their edges of weight 1 to the graph."""
        for entry in graph_data:
            self.addEdge(entry[0],entry[1],1)

    def getVertices(self):
        """returns the vertex matrix"""
        return self.vertices

    def getEdges(self, vertex):
        """returns the the edges for a single vertex"""
        return self.vertices[vertex-1]

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
