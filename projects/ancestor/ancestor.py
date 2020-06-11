
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

class Stack:
    def __init__(self):
        self.stack = []
    def push(self, value):
        self.stack.append(value)
    def pop(self):
        if self.size() > 0:
            return self.stack.pop()
        else:
            return None
    def size(self):
        return len(self.stack)

class Graph:
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex_id):
        # This initializes a blank set at the added id
        self.vertices[vertex_id] = set()

    def add_edge(self, v1, v2):
        # Perform only if both vertices are in the graph.
        if v1 in self.vertices and v2 in self.vertices:
            # Add v2 to the set in the hash table at v1.
            self.vertices[v1].add(v2)

    def get_neighbors(self, vertex_id):
        # Return all the edges of a given vertex
        return self.vertices[vertex_id]


def get_neighbors(arr, node):

    # Initialize a neighbors array
    neighbors = []

    # For each i in range(len(arr))
    for i in range(len(arr)):

        # If the second value of i is the node
        if arr[i][1] == node:
            # Add the key to neighbors.
            neighbors.append(arr[i][0])

    # When that is done return all neighbors
    return neighbors

# def earliest_ancestor(ancestors, starting_node):
#     # # FIFO
#     # Initialize a Queue
#     q = Queue()
#     # Create a set for the visited elements
#     visited = set()
#     # Create a levels array of empty None values
#     levels = [None] * (len(ancestors)*2)
#     # Append the starting path to the queue
#     q.enqueue([starting_node])
#     # At the key starting_node set it = to zero
#     levels[starting_node] = 0
#     # Mark that we've visited the starting node
#     visited.add(starting_node)
#     # While the queue size is not zero
#     while q.size() > 0:
#         # Strip off the first path
#         path = q.dequeue()
#         # The current node is the last value of the path
#         current = path[-1]
#         # For each neighbor in get_neighbors of current
#         for neighbor in get_neighbors(ancestors, current):
#             # This searches current for which neighbor is matching the current node. In our case it's matching 1 to 10.
#             print("Neighbor", neighbor)
#             if neighbor not in visited:
#                 #  Here we're creating a new path as a list
#                 new_path = list(path)
#                 # Append the neighbor
#                 new_path.append(neighbor)
#                 # Enqueue the new path
#                 q.enqueue(new_path)
#                 #  Change the level, which is None, to the level of current + 1 
#                 print("levels before", levels)
#                 levels[neighbor] = levels[current] + 1
#                 print("levels after", levels)
#                 visited.add(neighbor)
#     nodes = { key: val for key, val in enumerate(levels) if val is not None }
#     farthest = 0
#     for key in nodes:
#         if nodes[key] > farthest:
#             farthest = nodes[key]
#     farthest_nodes = []
#     for key in nodes:
#         if nodes[key] == farthest and farthest != 0:
#             farthest_nodes.append(key)
#     if len(farthest_nodes) >= 1:
#         return farthest_nodes[0]
#     else:
#         return -1

# Leana's solution

def earliest_ancestor(ancestors, starting_node):
    # Initialize a graph
    g = Graph()
    # Populate the graph with data
    for i in ancestors:
        g.add_vertex(i[0])
        g.add_vertex(i[1])
        g.add_edge(i[1], i[0])
    # Implement a Stack
    s = Stack()
    # Push a list with the starting_node
    s.push([starting_node])
    # Create a visited set
    visited = set()
    # Add the starting node to visited because we've seen it.
    visited.add(starting_node)
    # Becase we have the first node, that is the longest path
    longest_path = 1
    # This means there is no ancestor because we haven't found one yet.
    ancestor = -1
    # Just a print to see what is happening.
    print('GRAPH', g.vertices)
    # While the size of the stack is greater than 0
    while s.size() > 0:
        # Grab off the last list 
        path = s.pop()
        # Grab the last vertex from the popped path.
        node = path[-1]
        # If the length of get_neighbors is not 0
        if len(g.get_neighbors(node)) == 0:
            # Check if the len of path is more than longest path
            if longest_path < len(path):
                # Set longest path to the len of path.
                longest_path = len(path)
                # The ancestor is now node
                ancestor = node
            # If the longest path is the len of path
            elif longest_path == len(path):
                # Grab the smallest value of node vs ancestor
                # Set as ancestor
                ancestor = min(node, ancestor)
        # If the length of get_neighbors is more than zero
        else:
            # Neighbors is value of the node neighbors
            neighbors = g.get_neighbors(node)
            # For each neighbor
            for neighbor in neighbors:
                # Check if the neighbor has been seen before.
                if neighbor not in visited:
                    # Create a copy of the path as a list
                    copy = list(path)
                    # Append the neighbor to the copy
                    copy.append(neighbor)
                    # Add the copy list to the stack
                    s.push(copy)
                    # Add neighbor to visited since we've now seen it
                    visited.add(neighbor)

    # This is the base case where there are no neighbors
    if ancestor == -1:
        return -1

    # Otherwise just return the ancestor
    return ancestor






test_ancestors = [(1, 3), (2, 3), (3, 6), (5, 6), (5, 7), (4, 5), (4, 8), (8, 9), (11, 8), (10, 1)]
print(earliest_ancestor(test_ancestors, 3)) # Should be 10