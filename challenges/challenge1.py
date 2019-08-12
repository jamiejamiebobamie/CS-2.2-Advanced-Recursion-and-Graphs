from collections import deque as d
import sys
"""Challenge 1
- Implement the Graph ADT with an adjacency list
- Implement the Graph ADT with an adjacency matrix
- Implement code to read in a graph from a text file to create an instance
    of the Graph ADT and use it's methods.
- Test your code.
"""

"""
Git Issues:

 -ADDED UNITTESTS WITH THE UNITTEST MODULE, BUT HAD TROUBLE OVERRIDING
    THE __INIT__ FUNCTION. RE-RAN ORIGINAL TEST FILE WITH NEW METHOD NAMES
    AND RECIEVED THIS OUTPUT:
                ➜  challenges git:(master) ✗ python3 challenge1_test.py

                testing linked list implementation...
                all linked-list-graph tests pass

                testing adjacenecy matrix implementation...
                all adjacenecy matrix graph tests pass

    (TO YOUR COMMENTS: "test file runs" AND "test code does not run")

 -ADDED THE 'Graph' CLASS WHICH USES A DICTIONARY:
    "Use a dictionary to represent the adjacency list - no need to implement a
    LinkedList here."

 -ADDED DOC STRINGS TO ALL METHODS: "all methods need doc strings"
 (ONLY MY __INIT__ METHODS NEEDED THEM...)

 -CHANGED ALL METHODS TO SNAKE CASE: "snake_case for method names"
 (DID NOT CHANGE CLASS NAMES TO SNAKE CASE)

 -WHICH SAMPLE INPUT? THIS IS ON THE REPO IN THE CHALLENGES FILE:
                1,2,3,4
                (1,2)
                (1,4)
                (2,3)
                (2,4)

    "graph_data.txt" contains the above sample input.
    (TO YOUR COMMENT: "code runs on provided sample input")

 -ADDED COMMENTS TO ALL CODE: "code is well documented"

 -ADDED ERROR HANDLING TO SOME METHODS IN THE FORM OF CONDITIONALS:
    "error handling"

 -ADDED DRIVER CODE.

 """


def read_graph(filepath):
    """input file should be of form:
        1,2,3,4
        (1,2)
        (1,4)
        (2,3)
        (2,4)
    returns an array of vertices (ints) and and array of edges
    (tuple of two vertices: source to target)
    """
    edges = []
    listOfVertices = []

    with open(filepath, "r") as f:
        entries = f.read().split("\n")
    for i, entry in enumerate(entries):
        # the first entry is a list of vertices
        if i == 0:
            # parse the string to get all numbers
            listOfVertices = entry.split(",")
            # takes into account empty lines
        elif len(entry) > 0:
            # this assumes the graph IS directed (a digraph)
            edges.append((int(entry[1]), int(entry[3])))
    return listOfVertices, edges


class Vertex(object):
    """ Vertex Class
        A helper class for the Graph class that
        defines vertices and vertex neighbors.
    """
    def __init__(self, vertex):
        """initialize a vertex and its neighbors
        neighbors: set of vertices adjacent to self,
        stored in a dictionary with key = vertex,
        value = weight of edge between self and neighbor.
        """
        self.id = vertex
        # string
        self.neighbors = {}
        # dictionary of vertex_id's to int weights

    def add_neighbor(self, vertex, weight=0):
        """add a neighbor along a weighted edge"""
        if vertex not in self.neighbors:
            self.neighbors[vertex] = weight
            # add vertex-weight to self.neighbors dictionary

    def __str__(self):
        """output the list of neighbors of this vertex"""
        return (str(self.id) +
                " adjancent to "+str([x.id for x in self.neighbors]))

    def get_neighbors(self):
        """return the neighbors of this vertex"""
        # get all of the keys from the neighbors dictionary,
        # keys == vertex_id strings
        return self.neighbors.keys()

    def get_id(self):
        """return the id of this vertex"""
        return self.id
        # get the vertex's id, a string

    def get_edge_weight(self, vertex):
        """"return the weight of this edge"""
        # return the weight of a given vertex if the vertex is present
        # in the self.neighbors dictionary
        return self.neighbors[vertex] if self.neighbors[vertex] else None


class Graph:
    """ Graph Class
    A class demonstrating the essential
    facts and functionalities of graphs.
    """
    def __init__(self):
        """ initializes a graph object with an empty dictionary.
        """
        self.vertList = {}
        # a dictionary of vertex_id's to vertex objects
        self.numVertices = 0

    def add_vertex(self, key):
        """add a new vertex object to the graph with
        the given key and return the vertex
        """
        self.numVertices += 1
        # increment the count of number of vertices
        new_vertex = Vertex(key)
        # create a new vertex object with the given vertex_id
        self.vertList[key] = new_vertex
        # add the vertex to the dictionary of self.vertList as vertex_id :
        # vertex object
        return self.vertList[key]
        # return the vertex object

    def get_vertex(self, n):
        """return the vertex if it exists
            return the vertex if the vertex is present
            in the self.vertList dictionary
        """

        return self.vertList[n] if self.vertList[n] else None

    def add_edge(self, f, t, cost=0):
        """add an edge from vertex f to vertex t with a cost
        """
        if not self.vertList[f]:
            # if the from_vert is not in the self.vertList
            new_vertex = Vertex(f)
        # make a new vertex object
            self.vertList[f] = new_vertex
        # add it to the self.vertList
        if not self.vertList[t]:
            # if the to_vert is not in the self.vertList
            new_vertex = Vertex(t)
            # make a new vertex object
            self.vertList[t] = new_vertex
        # add it to the self.vertList
        self.vertList[f].add_neighbor(t, cost)
        # add the to_vert to the from_vert's neighbors dictionary with a weight

    def get_vertices(self):
        """return all the vertices in the graph"""
        return self.vertList.keys()
        # return all of the keys in the self.vertList dictionary,
        # string vertex_ids

    def __iter__(self):
        """iterate over the vertex objects in the
        graph, to use sytax: for v in g
        """
        result = []
        for v in self.vertList:
            result.append((v, self.vertList[v].get_neighbors()))
        return result
        # return all of the vertex objects of the graph


class AMGraph(object):
    """An Graph ADT with adjacency matrix.
    """
    def __init__(self, numberOfVertices):
        """ initializes a graph object with a matrix of 0's for the weights.
        """
        self.numberOfVertices = numberOfVertices
        self.vertices = [
            [0]*self.numberOfVertices for _ in range(self.numberOfVertices)
                ]

    def add_vertex(self, n=1):
        """increases the number of vertices by n.
        adds new edges of weight 0 to each of the existing vertices.
        adds the new vertices to the end of the vertex matrix.
        """
        number = int(n)
        # cast the number to an int regardless.
        self.numberOfVertices += number
        # increment the self.numberOfVertices by the number
        for vertex in self.vertices:
            # iterate through the self.vertices
            addVertices = [0]*number
            # add a new row of 0's to the adjacenet matrix
            vertex.extend(addVertices)
        self.vertices.append([0]*self.numberOfVertices)

    def add_edge(self, vFrom, vTo, weight=1):
        """adds a directed edge from a vertex to a vertex with a given weight
        """
        # check to make sure the vertices exist:
        if (vFrom-1 >= 0 and vTo-1 >= 0
                and vTo-1 <= self.numberOfVertices
                and vFrom-1 <= self.numberOfVertices):
            self.vertices[vFrom-1][vTo-1] = weight

    def add_edges(self, graph_data):
        """takes in an array of tuples (from_vert, to_vert)
        and adds their edges of weight 1 to the graph."""
        for entry in graph_data:
            self.add_edge(entry[0], entry[1], 1)

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
        # iterate through the input vertices, create a linked list object for
        # each vertex,
        # and insert the vertex into the self.vertices array
        for _ in range(self.numberOfVertices):
            new_LL = LinkedList(vertices[_])
            self.vertices.append(new_LL)

    def get_vertex(self, n):
        """returns the associated LinkedList object if it exists."""
        # check to ensure the given 'n' index is in
        # bounds of the self.vertices array
        # and then return the LL object at that index.
        return (self.vertices[n-1] if n-1 < self.numberOfVertices and n > 0
                else
                "Vertex index out of bounds." +
                "Please enter a vertex id between 1 and "
                + str(self.numberOfVertices) + ".")

    def get_vertices(self):
        """returns the id's/data of all the vertices in the graph"""
        # iterate through the self.vertices array
        # and append the vertex id's for each vertex
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
        """add an edge from vertex f (a number) to vertex t (a number)
        with a default cost/weight of 1
        """
        # check to ensure the vertex's exists in the self.vertices array
        # add the neighbor to the LL object with a target vertex
        # and a cost / weight
        if f-1 < self.numberOfVertices and f > 0:
            self.vertices[f-1].add_neighbor(t, cost)

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
        # append the LinkedList object's id's and their edges to the result
        # array.
        # return the result array
        for v in self.vertices:
            index = int(v.id)
            result.append([v.id, self.get_edges(index)])
        return result


class LinkedList(object):
    def __init__(self, vertex=None, head=None, tail=None):
        """ initializes a linked list object.
        """
        self.id = vertex
        # this is a string!
        self.length = 0
        self.head = head
        # the first vertex connected to the vertex at self.id.
        self.tail = tail

    def add_neighbor(self, data, weight=1):
        """Adds a single vertex to the linked list.
        """
        # initialize a new LinkedListNode
        new_vertex = LinkedListNode(data, weight)

        # check to see if the head is empty
        # if it is set the head and the tail to the new LinkedListNode
        if not self.head:
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

        # if the head is empty. there are no adjacent vertices.
        if not node:
            return "No out-going edges."

        # if there are more than two vertices in the list
        # iterate through them and return their data
        if self.head != self.tail:
            while node:
                result.append(node.data)
                node = node.next
            else:
                return result

        # if the head == the tail, there is only one vertex in the list.
        # return its data
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
        if not node:
            return "No out-going edges."

        # if there are more than two vertices in the list
        # iterate through them and return their data and weights
        if self.head != self.tail:
            while node:
                result.append((int(self.id), node.data, node.weight))
                node = node.next
            else:
                return result

        # if the head == the tail, there is only one vertex in the list.
        # return its data and weight
        else:
            return (int(self.id), node.data, node.weight)


class LinkedListNode(object):
    def __init__(self, data, weight=1):
        """ initializes a linked list node object.
        """
        self.data = data
        # string
        self.weight = weight
        # int
        self.next = None
        # pointer to LLNode object


if __name__ == "__main__":
    filePath = sys.argv[1]
    # filePath = "graph_data.txt"

    # read file. intialize vertices and edges.
    vertices, edges = read_graph(filePath)

    # make new graph object
    new = Graph()

    # add vertices
    for v in vertices:
        new.add_vertex(v)

    print(f"The vertices are: {new.get_vertices()} \n")

    # convert source vertex and target vertex integer id's to strings
    # add the edges to the respective dictionaries.
    for source, target in edges:
        source = str(source)
        target = str(target)
        new.add_edge(source, target)

    # iterating over vertices in the graph and returning the vertices
    # and their neighbors if a
    print("The edges are: ")
    print(new.__iter__())
