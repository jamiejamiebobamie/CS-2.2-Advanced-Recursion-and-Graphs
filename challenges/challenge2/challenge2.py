"""Challenge 2

Create a Challenge_2 folder in your challenge repository.
Copy any code you want to re-use from Challenge 1 to that folder before modifying.

Update your Graph ADT code to use Breadth-first Search to compute
the shortest path between two provided vertices in your graph.

Input: A graph file (containing an undirected, unweighted graph), a from_vertex and a to_vertex.

python3 challenge_2.py graph_data.txt 1 5


G
1,2,3,4,5
(1,2)
(1,4)
(2,3)
(2,4)
(2,5)
(3,5)

Output: The vertices in a shortest path from from_vertex to to_vertex
        and the number of edges in that path.

Vertices in shortest path: 1,2,5
Number of edges in shortest path: 3"""

from collections import deque
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
    returns an array of vertices (ints) and and array of edges (tuple of two vertices: source to target)
    """

    edges = []
    listOfVertices = []
    graphType = ""

    with open(filepath, "r") as f:
        entries = f.read().split("\n")

    for i, entry in enumerate(entries):
        if i == 0: # the first entry is the type of the graph
            graphType = entry
        if i == 1: # the second entry is a list of vertices
            listOfVertices = entry.split(",") # parse the string to get all numbers
        if i > 1 and len(entry) > 0 and len(entry) == 5: # takes into account empty lines and lines not of the correct format
            edges.append((int(entry[1]), int(entry[3])))
            if graphType == "G": # an undirected graph has "mirrored" edges
                edges.append((int(entry[3]), int(entry[1])))

    return listOfVertices, edges

# filePath = '/Users/jamesmccrory/Documents/dev/CS-2.2-Advanced-Recursion-and-Graphs/challenges/challenge2/graph_data.txt'

class Graph(object):
    """An Graph ADT with adjacency matrix.
    """
    def __init__(self, numberOfVertices):
        self.numberOfVertices = numberOfVertices
        self.vertices = [[0]*self.numberOfVertices for _ in range(self.numberOfVertices)]

    def addVertex(self):
        """increases the number of vertices by one.
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

    def breadth_first_search(self, filepath, from_vert, to_vert):
        """Referenced: https://www.geeksforgeeks.org/breadth-first-search-or-bfs-for-a-graph/ for guidance.

            Input: A graph file (containing an undirected, unweighted graph), a from_vertex and a to_vertex.

            Output: The vertices in a shortest path from from_vertex to to_vertex
                    and the number of edges in that path.

            Example graph output:
                Vertices in shortest path: 1,2,5
                Number of edges in shortest path: 3
        """
        if from_vert < 1 or from_vert > self.numberOfVertices:
            raise Exception("Vertex out of bounds.")

        if to_vert < 1 or to_vert > self.numberOfVertices:
            raise Exception("Vertex out of bounds.")

        if self.vertices[from_vert-1][to_vert-1] == 1: # exit early if the to_vertex is adjacent to the from_vertex
            return "Vertices in shortest path: " + str(from_vert) + "," + str(to_vert) + "\n" + "Number of edges in shortest path: 1"

        result = []
        queue = deque()
        checkedArray = self.numberOfVertices * [False] # to keep track of vertices that have been visited already.

        queue.append(from_vert)
        checkedArray[from_vert-1] = True

        while queue:

            current = queue.popleft()
            result.append(current)
            if current == to_vert:
                # a list comprehension that takes the 'result' array and casts it to a string w/o adding a comma after the last item.
                result = [str(entry)+"," if i != len(result)-1 else str(entry) for i, entry in enumerate(result)]
                return "Vertices in shortest path: " + "".join(result) + "\n" + "Number of edges in shortest path: " + str(len(result)-1)

            for i, vertex in enumerate(self.vertices[current-1]):
                if vertex != 0 and checkedArray[i] == False:
                    queue.append(i+1)
                    checkedArray[i] = True

        return result


if __name__ == "__main__":
    filePath = sys.argv[1]
    from_vert = int(sys.argv[2])
    to_vert = int(sys.argv[3])

    data = readGraph(filePath)
    new = Graph(len(data[0]))
    new.addEdges(data[1])
    print(new.breadth_first_search(filePath, from_vert, to_vert))
