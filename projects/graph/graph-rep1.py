from util import Stack, Queue

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

    def bft(self, starting_vertex):
        # FIFO
        # Create an empty queue
        q = Queue()

        # Enqueue the start
        q.enqueue(starting_vertex)

        # Create a set to store the visited vertices
        visited = set()

        # While the queue is not empty
        while q.size() > 0:

            # Dequeue the first vertex
            v = q.dequeue()

            # If that vertex has not been visited
            if v not in visited:
                # Visit it
                print(v)

                # Mark as visited
                visited.add(v)

                # Get the neighbors and enqueue them.
                for next in self.get_neighbors(v):

                    # Enqueue the next value
                    q.enqueue(next)

    def dft(self, starting_vertex):
        # LIFO
        # Create an empty stack
        s = Stack()

        # Push the start
        s.push(starting_vertex)

        # Create a set to store the visited vertices
        visited = set()

        # While the stack is not empty
        while s.size() > 0:

            # Pop the last vertex
            v = s.pop()

            # If that vertex has not been visited
            if v not in visited:
                
                # Visit it
                print(v)

                # Mark as visited
                visited.add(v)

                # Get the neighbors and push them to the stack.
                for next in self.get_neighbors(v):
                    s.push(next)

    def bfs(self, starting_vertex, destination_vertex):
        #FIFO
        # Create an empty queue and enqueue the starting vertex as a list. This will kick off our path.
        q = Queue()
        path = [starting_vertex]
        q.enqueue(path)

        # Create a set to store visited vertices
        visited = set()

        # While the queue is not empty
        while q.size() > 0:
            # Dequeue the first list (path)
            path_list = q.dequeue()

            # Grab the last vertex from the list
            last_vertex = path_list[-1]

            if last_vertex is destination_vertex:
                return path_list

            # If the vertex has not been visited
            if last_vertex not in visited:

                # Add the vertex to visited and move
                visited.add(last_vertex)

                for next in self.get_neighbors(last_vertex):

                    # Create a copy of the path_list
                    path_copy = path_list[:]

                    # Append the next vertex to the path_copy.
                    path_copy.append(next)

                    # This will kick off the search again having added the new path.
                    q.enqueue(path_copy)

    def dfs(self, starting_vertex, destination_vertex):
        # LIFO
        # Create an empty stack and push the starting vertex as a list. This will kick off our path.
        s = Stack()
        path = [starting_vertex]
        s.push(path)

        # Create a set to store visited vertices
        visited = set()

        # While the stack is not empty
        while s.size() > 0:
            # Pop the first list (path)
            path_list = s.pop()

            # Grab the last vertex from the list
            last_vertex = path_list[-1]

            if last_vertex is destination_vertex:
                return path_list

            # If the vertex has not been visited
            if last_vertex not in visited:

                # Add the vertex to visited and move
                visited.add(last_vertex)

                for next in self.get_neighbors(last_vertex):
                    # Create a copy of the path_list
                    path_copy = path_list[:]

                    # Append the next vertex to the path_copy
                    path_copy.append(next)

                    # This will kick off the search again having added the new path.
                    s.push(path_copy)

    def dfs_recursive(self, starting_vertex, destination_vertex):
        pass

    def dft_recursive(self, starting_vertex):
        pass


if __name__ == '__main__':
    graph = Graph()  # Instantiate your graph
    # https://github.com/LambdaSchool/Graphs/blob/master/objectives/breadth-first-search/img/bfs-visit-order.png
    graph.add_vertex(1)
    graph.add_vertex(2)
    graph.add_vertex(3)
    graph.add_vertex(4)
    graph.add_vertex(5)
    graph.add_vertex(6)
    graph.add_vertex(7)
    graph.add_edge(5, 3)
    graph.add_edge(6, 3)
    graph.add_edge(7, 1)
    graph.add_edge(4, 7)
    graph.add_edge(1, 2)
    graph.add_edge(7, 6)
    graph.add_edge(2, 4)
    graph.add_edge(3, 5)
    graph.add_edge(2, 3)
    graph.add_edge(4, 6)

    '''
    Should print:
        {1: {2}, 2: {3, 4}, 3: {5}, 4: {6, 7}, 5: {3}, 6: {3}, 7: {1, 6}}
    '''
    print(graph.vertices)

    '''
    Valid BFT paths:
        1, 2, 3, 4, 5, 6, 7
        1, 2, 3, 4, 5, 7, 6
        1, 2, 3, 4, 6, 7, 5
        1, 2, 3, 4, 6, 5, 7
        1, 2, 3, 4, 7, 6, 5
        1, 2, 3, 4, 7, 5, 6
        1, 2, 4, 3, 5, 6, 7
        1, 2, 4, 3, 5, 7, 6
        1, 2, 4, 3, 6, 7, 5
        1, 2, 4, 3, 6, 5, 7
        1, 2, 4, 3, 7, 6, 5
        1, 2, 4, 3, 7, 5, 6
    '''
    graph.bft(1)

    '''
    Valid DFT paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    graph.dft(1)
    graph.dft_recursive(1)

    '''
    Valid BFS path:
        [1, 2, 4, 6]
    '''
    print(graph.bfs(1, 6))

    '''
    Valid DFS paths:
        [1, 2, 4, 6]
        [1, 2, 4, 7, 6]
    '''
    print(graph.dfs(1, 6))
    print(graph.dfs_recursive(1, 6))