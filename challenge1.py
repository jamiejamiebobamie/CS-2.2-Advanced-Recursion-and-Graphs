"""# Challenges
- Unless otherwise stated, use simple concrete data types in your implementations (lists).
Stretch challenges will give you an opportunity to refactor
with collections and more complex data types.

- Graphs will be defined in a text file with the first line being a list of vertices,
followed by one vertex pair per line representing the edges.

```
1,2,3,4
(1,2)
(1,4)
(2,3)
(2,4)
```

## Challenge 1
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
            for i, v in enumerate(entry):
                if not i % 2: # parse the string to get all numbers
                    listOfVertices.append(int(v))
        elif len(entry) > 0: # takes into account empty lines
            edges.append((int(entry[1]), int(entry[3])))

    return listOfVertices, edges

class Graph(object):
    """An Graph ADT with adjacency matrix.
    """
    def __init__(self, numberOfVertices):
        self.numberOfVertices = numberOfVertices
        self.vertices = [[0]*self.numberOfVertices for _ in range(self.numberOfVertices)]

    def addVertex(self):
        """increases the number of vertexes by one.
        adds a new edge of weight 0 to each of the existing vertices.
        adds the new vertex to the end of the vertex matrix.
        """
        self.numberOfVertices += 1
        for vertex in self.vertices:
            vertex.append(0)
        self.vertices.append([0]*self.numberOfVertices)

    def addEdge(self,vFrom, vTo, weight):
        """adds a directed edge from a vertex to a vertex with a given weight"""
        # check to make sure the vertices exist
        if vFrom-1 >= 0 and vTo-1 >= 0 and vTo-1 <= self.numberOfVertices and vFrom-1 <= self.numberOfVertices:
            self.vertices[vFrom-1][vTo-1] = weight

    def getVertices(self):
        """returns the vertex matrix"""
        return self.vertices

    def getEdges(self, vertex):
        """returns the the edges for a single vertex"""
        return self.vertices[vertex-1]


class Graph(object):
    """An Graph ADT with adjacency list.
    Graph -> LinkedList -> LinkedListNode(s)
    """
    def __init__(self, numberOfVertices):
        self.numberOfVertices = numberOfVertices
        self.vertices = [[0]*self.numberOfVertices for _ in range(self.numberOfVertices)]

    def getVertex(self, n):
        """returns the associated LinkedList object if it exists."""
        return self.vertices[n-1] if self.vertices[n-1] else None

    def addEdge(self, f, t, cost=0):
        """add an edge from vertex f (a number) to vertex t (a number) with a cost
        """
        pass
        # if f-1 => 0 and f-1 < self.numberOfVertices:
        #     node = self.vertices[f-1].head
        #     while node:
        #         if node.data == t:
        #             node.edge = weight

        #     self.vertList[f] = new_vertex
        # if not self.vertList[t]:
        #     new_vertex = Vertex(t)
        #     self.vertList[t] = new_vertex
        # self.vertList[f].addNeighbor(t,cost)

    def getVertices(self):
        """return all the vertices in the graph"""
        return self.vertList.keys()

    def __iter__(self):
        """iterate over the vertex objects in the
        graph, to use sytax: for v in g
        """
        return iter(self.vertList.values())


    def addVertex(self):
        """increases the number of vertexes by one.
        adds a new edge of weight 0 to each of the existing vertices.
        adds the new vertex to the end of the vertex matrix.
        """
        self.numberOfVertices += 1
        for vertex in self.vertices:
            vertex.append(0)
        self.vertices.append([0]*self.numberOfVertices)

    def addEdge(self,vFrom, vTo, weight):
        """adds a directed edge from a vertex to a vertex with a given weight"""
        pass
        # check to make sure the vertices exist
        # if vFrom-1 >= 0 and vTo-1 >= 0 and vTo-1 <= self.numberOfVertices and vFrom-1 <= self.numberOfVertices:
            # self.vertices[vFrom-1][vTo-1] = weight

    def getVertices(self):
        """returns the vertex matrix"""
        return self.vertices

    def getEdges(self, vertex):
        """returns the the edges for a single vertex"""
        return self.vertices[vertex-1]


class LinkedList(object):
    def __init__(self, vertex, head=None, tail=None):
        self.id = vertex
        self.length = 0
        self.head = head # the first vertex connected to the vertex at self.id
        self.tail = tail

    def addNeighbor(self,data):
        new_vertex = LinkedListNode(object)

    # def addEdge(vertex,)

    def addVertices(self, dataArray):
        """Add a series of vertices.
        """
        previous = None
        for data in dataArray:
            new_node = LinkedListNode(data)
            if previous:
                previous.next = new_node
            self.length += 1
            previous = new_node

class LinkedListNode(object):
    def __init__(self, data, next=None, weight=None):
        self.data = data
        self.weight = weight
        self.next = next
