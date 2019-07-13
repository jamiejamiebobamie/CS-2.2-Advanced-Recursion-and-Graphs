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


class Graph(object):
    """An Graph ADT with adjacency matrix.
    """
    def __init__(self, numberOfVertices):
        self.numberOfVertices = numberOfVertices
        self.vertices = [[0]*self.numberOfVertices for _ in range(self.numberOfVertices)]
        # for _ in range(self.numberOfVertices):
        #     self.vertices.append([0*self.numberOfVertices])

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
    """
    def __init__(self, numberOfVertices):
        self.numberOfVertices = numberOfVertices
        self.vertices = [[0]*self.numberOfVertices for _ in range(self.numberOfVertices)]
        # for _ in range(self.numberOfVertices):
        #     self.vertices.append([0*self.numberOfVertices])

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
