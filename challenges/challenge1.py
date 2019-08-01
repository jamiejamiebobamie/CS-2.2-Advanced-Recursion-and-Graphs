"""Challenge 1
- Implement the Graph ADT with an adjacency list
- Implement the Graph ADT with an adjacency matrix
- Implement code to read in a graph from a text file to create an instance of the Graph ADT and use it's methods.
- Test your code.
"""

"""
Git Issues:

 -RE-RAN TEST FILE WITH NEW METHOD NAMES AND RECIEVED THIS OUTPUT:
                ➜  challenges git:(master) ✗ python3 challenge1_test.py

                testing linked list implementation...
                all linked-list-graph tests pass

                testing adjacenecy matrix implementation...
                all adjacenecy matrix graph tests pass


    (TO YOUR COMMENTS: "test file runs" AND "test code does not run")

 -ADDED THE 'Graph' CLASS WHICH USES A DICTIONARY: "Use a dictionary to represent the adjacency list - no need to implement a LinkedList here."

 -ADDED DOC STRINGS TO ALL METHODS: "all methods need doc strings" (ONLY MY __INIT__ METHODS NEEDED THEM...)

 -CHANGED ALL METHODS TO SNAKE CASE: "snake_case for method names" (DID NOT CHANGE CLASS NAMES TO SNAKE CASE)

 -WHICH SAMPLE INPUT? THIS IS ON THE REPO IN THE CHALLENGES FILE:
                1,2,3,4
                (1,2)
                (1,4)
                (2,3)
                (2,4)

    "graph_data.txt" contains the above sample input.
    (TO YOUR COMMENT: "code runs on provided sample input")

 code is well documented
 error handling

 -ADDED DRIVER CODE.

 """

from collections import deque as d


def read_graph(filepath):
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

""" Vertex Class
A helper class for the Graph class that defines vertices and vertex neighbors.
"""
class Vertex(object):

    def __init__(self, vertex):
        """initialize a vertex and its neighbors
        neighbors: set of vertices adjacent to self,
        stored in a dictionary with key = vertex,
        value = weight of edge between self and neighbor.
        """
        self.id = vertex
        self.neighbors = {}

    def add_neighbor(self, vertex, weight=0):
        """add a neighbor along a weighted edge"""
        if vertex not in self.neighbors:
            self.neighbors[vertex] = weight

    def __str__(self):
        """output the list of neighbors of this vertex"""
        return str(self.id) + " adjancent to " + str([x.id for x in self.neighbors])

    def get_neighbors(self):
        """return the neighbors of this vertex"""
        result = []
        for key in self.neighbors.keys():
            result.append(key)
        return result

    def get_id(self):
        """return the id of this vertex"""
        return self.id

    def get_edge_weight(self, vertex):
        """"return the weight of this edge"""
        return self.neighbors[vertex] if self.neighbors[vertex] else None

""" Graph Class
A class demonstrating the essential
facts and functionalities of graphs.
"""

class Graph:
    """ Feedback from Challenge 1:

        'Use a dictionary to represent the adjacency list - no need to implement a LinkedList here.
        No output - readGraph method is never called.'

        Implementing the graph with a dictionary of array vertex objects as values:

    """
    def __init__(self):
        """ initializes a graph object with an empty dictionary.
        """
        self.vertList = {}
        self.numVertices = 0

    def add_vertex(self, key):
        """add a new vertex object to the graph with
        the given key and return the vertex
        """
        self.numVertices += 1
        new_vertex = Vertex(key)
        self.vertList[key] = new_vertex
        return self.vertList[key]

    def get_vertex(self, n):
        """return the vertex if it exists"""
        return self.vertList[n] if self.vertList[n] else None

    def add_edge(self, f, t, cost=0):
        """add an edge from vertex f to vertex t with a cost
        """
        if not self.vertList[f]:
            new_vertex = Vertex(f)
            self.vertList[f] = new_vertex
        if not self.vertList[t]:
            new_vertex = Vertex(t)
            self.vertList[t] = new_vertex
        self.vertList[f].add_neighbor(t,cost)

    def get_vertices(self):
        """return all the vertices in the graph"""
        return self.vertList.keys()

    def __iter__(self):
        """iterate over the vertex objects in the
        graph, to use sytax: for v in g
        """
        result = []
        for v in self.vertList:
            result.append((v, self.vertList[v].get_neighbors()))
        return result

class AMGraph(object):
    """An Graph ADT with adjacency matrix.
    """
    def __init__(self, numberOfVertices):
        """ initializes a graph object with a matrix of 0's for the weights.
        """
        self.numberOfVertices = numberOfVertices
        self.vertices = [[0]*self.numberOfVertices for _ in range(self.numberOfVertices)]

    def add_vertex(self, n=1):
        """increases the number of vertices by n.
        adds new edges of weight 0 to each of the existing vertices.
        adds the new vertices to the end of the vertex matrix.
        """
        number = int(n) #   cast the number to an int regardless.
        self.numberOfVertices += number
        for vertex in self.vertices:
            addVertices = [0]*number
            vertex.extend(addVertices)
        self.vertices.append([0]*self.numberOfVertices)

    def add_edge(self,vFrom, vTo, weight=1):
        """adds a directed edge from a vertex to a vertex with a given weight"""
        # check to make sure the vertices exist:
        if vFrom-1 >= 0 and vTo-1 >= 0 and vTo-1 <= self.numberOfVertices and vFrom-1 <= self.numberOfVertices:
            self.vertices[vFrom-1][vTo-1] = weight

    def add_edges(self, graph_data):
        """takes in an array of tuples (from_vert, to_vert) and adds their edges of weight 1 to the graph."""
        for entry in graph_data:
            self.add_edge(entry[0],entry[1],1)

    def get_vertices(self):
        """returns the vertex matrix"""
        return self.vertices

    def get_edges(self, vertex):
        """returns the the edges for a single vertex"""
        return self.vertices[vertex-1]

class LLGraph(object):
    """An Graph ADT with adjacency list.
    Graph -> LinkedList -> LinkedListNode(s)
    """
    def __init__(self, vertices=None):
        """ initializes a graph object with an array of linked list objects.
        """
        self.numberOfVertices = len(vertices)
        self.vertices = []
        # iterate through the input vertices, create a linked list object for each vertex, and insert the vertex into the self.vertices array
        for _ in range(self.numberOfVertices):
            new_LL = LinkedList(vertices[_])
            self.vertices.append(new_LL)

    def get_vertex(self, n):
        """returns the associated LinkedList object if it exists."""
        # check to ensure the given 'n' index is in bounds of the self.vertices array and then return the LL object at that index.
        return self.vertices[n-1] if n-1 < self.numberOfVertices and n > 0 else "Vertex index out of bounds. Please enter a vertex id between 1 and " + str(self.numberOfVertices) + "."

    def get_vertices(self):
        """returns the id's/data of all the vertices in the graph"""
        # iterate through the self.vertices array and append the vertex id's for each vertex
        # reutrn the array of vertex ids
        result = []
        for v in self.vertices:
            result.append(v.id)
        return result

    def get_neighbors_of_a_vertex(self, vertex):
        """returns the id's/data of all of the neighbors of a given vertex."""
        # check to ensure the vertex's exists in the self.vertices array
        # return the neighbors associated with that vertex
        if vertex > 0 and vertex-1 < self.numberOfVertices:
            return self.vertices[vertex-1].get_neighbors()

    def get_edges(self, vertex):
        """returns the the edges for a single vertex"""
        # check to ensure the vertex's exists in the self.vertices array
        # return the edge associated with that vertex
        if vertex-1 < self.numberOfVertices and vertex > 0:
            return self.vertices[vertex-1].get_edges()

    def add_edge(self, f, t, cost=1):
        """add an edge from vertex f (a number) to vertex t (a number) with a default cost/weight of 1
        """
        # check to ensure the vertex's exists in the self.vertices array
        # add the neighbor to the LL object with a target vertex and a cost / weight
        if f-1 < self.numberOfVertices and f > 0:
            self.vertices[f-1].add_neighbor(t,cost)

    def add_edges(self, edgeData):
        """add the edges from an array of edge data.
        the array should look like:
        [
            ( from_vert, to_vert, optional_weight ) , ...
                                                            ]
        """
        # iterate through the edgeData array
        # add the new edges using the graph's add_edge method
        for edge in edgeData:
            self.add_edge(*edge)

    def add_vertex(self):
        """increases the number of vertices by one.
        adds a new edge of weight 0 to each of the existing vertices.
        adds the new vertex to the end of the vertex matrix.
        """
        # increment the numberOfVertices value by one
        # intialize a new linkedlist object
        # append the LL object to the end of the self.vertices array
        self.numberOfVertices += 1
        new_linked_list = LinkedList(str(self.numberOfVertices))
        self.vertices.append(new_linked_list)

    def __iter__(self):
        """iterate over the vertex objects in the
        graph, to use sytax: for v in g
        """
        result = []
        # iterate through the array of linkedlist objects
        # append the LinkedList object's id's and their edges to the result array
        # return the result array
        for v in self.vertices:
            index = int(v.id)
            result.append([v.id, self.get_edges(index)])
        return result

class LinkedList(object):
    def __init__(self, vertex=None, head=None, tail=None):
        """ initializes a linked list object.
        """
        self.id = vertex # this is a string!
        self.length = 0
        self.head = head # the first vertex connected to the vertex at self.id.
        self.tail = tail

    def add_neighbor(self,data, weight=1):
        """Adds a single vertex to the linked list.
        """
        # initialize a new LinkedListNode
        new_vertex = LinkedListNode(data, weight)

        # check to see if the head is empty
        # if it is set the head and the tail to the new LinkedListNode
        if self.head == None:
            self.head = self.tail = new_vertex

        # if the head == the tail, set the new LinkedListNode to be the tail
        # set the head's next node to the new LinkedListNode
        elif self.head == self.tail:
            self.tail = new_vertex
            self.head.next = new_vertex

        # otherwise there are more than two nodes in the list
        # set the current tail's next value to point to the new LinkedListNode
        # set the new LinkedListNode to be the new tail
        else:
            self.tail.next = new_vertex
            self.tail = new_vertex
        self.length += 1

    def get_neighbors(self):
        """Returns a list of all of the adjacent vertices' ids/data.
        """

        result = []
        node = self.head

        # if the head is empty
        if node == None:
            return "No out-going edges."

        # if there are more than two vertices in the list
        # iterate through them and return their data
        if self.head != self.tail:
            while node:
                result.append(node.data)
                node = node.next
            else:
                return result

        # if the head == the tail, there is only one vertex in the list. return its data
        else:
            return (node.data)

        return result

    def get_edges(self):
        """Returns a list of all of the adjacent vertices in the form of:
            (current_vertex, target_vertex, weight of edge)
        """
        result = []
        node = self.head

        # if the head is empty
        if node == None:
            return "No out-going edges."

        # if there are more than two vertices in the list
        # iterate through them and return their data and weights
        if self.head != self.tail:
            while node:
                result.append((int(self.id),node.data,node.weight))
                node = node.next
            else:
                return result

        # if the head == the tail, there is only one vertex in the list. return its data and weight
        else:
            return (int(self.id),node.data,node.weight)

class LinkedListNode(object):
    def __init__(self, data, weight=1):
        """ initializes a linked list node object.
        """
        self.data = data
        self.weight = weight
        self.next = None


if __name__ == "__main__":
    filePath = "graph_data.txt"

    # read file. intialize vertices and edges.
    vertices, edges = read_graph(filePath)

    # make new graph object
    new = Graph()

    # add vertices
    for v in vertices:
        new.add_vertex(v)

    # convert source vertex and target vertex integer id's to strings
    # add the edges to the respective dictionaries.
    for source,target in edges:
        source = str(source)
        target = str(target)
        new.add_edge(source,target)

    # iterating over vertices in the graph and returning the vertices and their neighbors if any
    print(new.__iter__())
