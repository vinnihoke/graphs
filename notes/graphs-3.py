'''
Connected Components

Parts of the graph that are connected, but disjoint from other parts of the graph.

for each node:
    if node not visited:
        traverse from that node
        increment counter

'''
'''
for each node:
    if node not visited:
        traverse from that node
        increment counter

example visited matrix:
visited = [
    [False, False,False,False,False],
    [False, False,False,False,False],
    [False, False,False,False,False],
    [False, False,False,False,False],
    [False, False,False,False,False],
]
'''


islands = [
    [0, 1, 0, 1, 0],
    [1, 1, 0, 1, 1],
    [0, 0, 1, 0, 0],
    [1, 0, 1, 0, 0],
    [1, 1, 0, 0, 0],
]

# Islands is an example of a 2d array.

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

def get_neighbors(row, col, matrix):
    neighbors = []

    # First check if each is in range.
    # Check North
    if row > 0 and matrix[row - 1][col] == 1:
        neighbors.append((row - 1, col))

    # Check South
    if row < len(matrix) - 1 and matrix[row + 1][col] == 1:
        neighbors.append((row + 1, col))
        
    # Check West
    if col > 0 and matrix[row][col - 1] == 1:
        neighbors.append((row, col - 1))

    # Check East
    if col < len(matrix[0]) - 1 and matrix[row][col + 1] == 1:
        neighbors.append((row, col + 1))

    return neighbors

def dft(row, col, matrix, visited):
    s = Stack()

    s.push((row, col)) # Storing as a tuple
    while s.size() > 0:
        row, col = s.pop() # Pulling and destructuring
        if not visited[row][col]:
            visited[row][col] = True

            for neighbor in get_neighbors(row, col, matrix):
                s.push(neighbor)

def island_counter(matrix):  # Matrix is a 2D array, list of lists.
    # Create a visited matrix
    visited = []
    island_counter = 0

    # See visited above
    for _ in range(len(matrix)):
        visited.append([False] * len(matrix[0]))

    # Walk through each cell in the matrix
    for row in range(len(matrix)):
        for col in range(len(matrix[row])):

            # If it's not visited
            if not visited[row][col]:

                # If it's a "1"
                if matrix[row][col] == 1:

                    # Do DFT and mark them as visited
                    dft(row, col, matrix, visited)

                    # Increment counter by 1
                    island_counter += 1

    # return counter
    return island_counter


print(island_counter(islands))  # 4


class Graph:

    # ... 

    def populate_graph(self, num_users, avg_friendships):
        self.users = {} # Nodes
        self.friendships = {} # Edges

        # Add users
        for i in range(num_users):
            self.addUser(f"User {i}")

        # Generate all possible friendships

        # Shuffle all possible friendships

        # Go through the list of shuffled friendships, adding the right number of them to reach the avg_friendships.