'''
Nodes == verts == vertices == vertexes
    These are the things that store the data

Nodes connected by edges
    Edges can be directional

If a graph has directional edges, it's called a "directed graph".

Keep track of what node has been visited. 

    * Visited flag
    * Hash Table
    * Set

    We are creating a stack so LIFO.
    Pop off the top of the stack, then mark it as visited. 
        Do what you need to do, then visit it's neighbors.


Depth first traversal

Push starting node on stack
while stack isn't empty:
    pop the node off the top of the stack
    if the node isn't visited:
        visit the node (example print it out)
        mark it as visited
        push all its neighbors on the stack

Bredth first traversal

Push starting node on queue
while queue isn't empty:
    pop the node off the top of the queue
    if the node isn't visited:
        visit the node (example print it out)
        mark it as visited
        push all its neighbors on the queue


Graph representations

How we store the graph in memory

1. Adjacency matrix
2. Adjacency list

A matrix is a grid.

    a   b   c   d   e   f   g   h
a       T       T               T

b           T

c       T                   T

d   T

e

f

g           T

h   T

List:

a [ b h d ]
b [ c a f e ]
c [ b g ]

Breadth first search
When you visit one node from another, keep track of those.
Or you can store then by adding the previous path to each node. This way each has a reference to the shortest distance.

'''


class Queue():
    def __init__(self):
        self.queue = []

    def enqueue(self, value):
        self.queue.append(value)

    def dequeue(self):
        if self.size() > 0:
            return self.queue.pop(0)
        else:
            return None

    def size(self):
        return len(self.queue)


class Graph:
    def __init__(self):
        self.vertices = {}

    # Add verts
    def add_vertex(self, vertex_id):
        # set of edges from this vert. Sets have O(1) lookup.
        self.vertices[vertex_id] = set()

    # Add edge
    def add_edge(self, v1, v2):
        if v1 in self.vertices and v2 in self.vertices:
            # Add is built in to sets. Add v2 as a neighbor to v1
            self.vertices[v1].add(v2)
        else:
            raise IndexError("Vertex doesn't exist")
    # Get neighbors

    def get_neighbors(self, vertex_id):
        return self.vertices[vertex_id]

    def bft(self, starting_vertex_id):
        # Create an empyt queue and enque the starting vertex id
        q = Queue()
        q.enqueue(starting_vertex_id)

        # Create a set to store visited vertices
        visited = set()

        # While the que is not empty
        while q.size() > 0:

            # Dequeue the first vertex
            v = q.dequeue()

            # If that vertex has not been visited
            if v not in visited:

                # Visit it
                print(v)

                # Mark it as visited
                visited.add(v)

                for next_vert in self.get_neighbors(v):
                    q.enqueue(next_vert)

    def dft(self, starting_vertex_id):

        # implement this with a stack rather than a queue.
        # Search means to get the item and path.


g = Graph()
g.add_vertex("A")
g.add_vertex("B")
g.add_vertex("C")

g.add_edge("B", "A")

# Must add the first edge, and second if we need 2 way binding.
g.add_edge("B", "C")
g.add_edge("C", "B")

# print(g.get_neighbors("B"))
# print(g.get_neighbors("C"))
# print(g.vertices)

g.bft("A")
