from room import Room
from player import Player
from world import World

import random
from ast import literal_eval

# Load world
world = World()


# You may uncomment the smaller graphs for development and testing purposes.

# map_file = "maps/test_line.txt"
# map_file = "maps/test_cross.txt"
map_file = "maps/test_loop.txt"
# map_file = "maps/test_loop_fork.txt"
# map_file = "maps/main_maze.txt"

# Loads the map into a dictionary
room_graph=literal_eval(open(map_file, "r").read())
world.load_graph(room_graph)

# Print an ASCII map
world.print_rooms()

player = Player(world.starting_room)

# Fill this out with directions to walk
# traversal_path = ['n', 'n']
# ? ------------------------------------- OBSERVATIONS 
# When total exits len is 1, we've hit the end of the path, time to reverse room.

# Store a path = {}
# Set the initial direction

# This would be more of a depth first. We want a breadth first search.
# If room is completed skip it and continue;
    # Otherwise find the next un-completed direction and change direction
        # Keep moving that direction until the list len is 1
        # Change to that direction
            # If room is completed skip it and continue
                # Otherwise find the next un-completed direction and change direction

'''
Cross has no loops.
{
    0: [(3, 5), {'n': 1, 's': 5, 'e': 3, 'w': 7}], 
    1: [(3, 6), {'s': 0, 'n': 2}],
    2: [(3, 7), {'s': 1}],
    3: [(4, 5), {'w': 0, 'e': 4}],
    4: [(5, 5), {'w': 3}],
    5: [(3, 4), {'n': 0, 's': 6}],
    6: [(3, 3), {'n': 5}],
    7: [(2, 5), {'w': 8, 'e': 0}],
    8: [(1, 5), {'e': 7}]
}

{
    0: [(3, 5), {'n': 1, 's': 5, 'e': 3, 'w': 7}],
    1: [(3, 6), {'s': 0, 'n': 2}],
    2: [(3, 7), {'s': 1}],
    3: [(4, 5), {'w': 0, 'e': 4}],
    4: [(5, 5), {'w': 3}],
    5: [(3, 4), {'n': 0, 's': 6}],
    6: [(3, 3), {'n': 5, 'w': 11}],
    7: [(2, 5), {'w': 8, 'e': 0}],
    8: [(1, 5), {'e': 7, 's': 9}],
    9: [(1, 4), {'n': 8, 's': 10}],
    10: [(1, 3), {'n': 9, 'e': 11}],
    11: [(2, 3), {'w': 10, 'e': 6}]
}
'''

# ! ------------------------------------- CODE STARTS HERE 
# Goal is to create a traversal path array of direction strings that traverses the entire map.
traversal_path = []

visited_rooms = set()
player.current_room = world.starting_room
visited_rooms.add(player.current_room)

# ! Use to kickoff the party. This should give a length.
# print(room_graph)

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
        self.previous_room_id = 0
        self.rooms = {}
        self.direction = "n"

    # def add_connection(self, room_id, next_id):
    #     # Creates a bi-directional connection
    #     if room_id == next_id:
    #         return False
    #     elif next_id in self.rooms[room_id] or room_id in self.rooms[next_id]:
    #         return False
    #     else:
    #         self.rooms[room_id].add(next_id)
    #         self.rooms[next_id].add(room_id)
    #         return True



    def populate_graph(self):
        opposites = {
            "n": "s",
            "s": "n",
            "w": "e",
            "e": "w"
        }
        for _ in range(8):

            # Good stopping point.
            # I think this needs some sort of tracking now. Have we visited here? If so, change direction to something other than the opposite.
            # Might need a stack of some kind?

            visited = set()

            if player.current_room.get_room_in_direction(self.direction) == None:
                self.direction = opposites[self.direction]

            current_id = player.current_room.id

            if current_id not in visited:
                print(visited)
                print("Current Room ID: ", current_id)
                print("Get exits :139 ", player.current_room.get_exits())
                self.rooms[current_id] = { key: "" for key in player.current_room.get_exits()}
                
                player.travel(self.direction)
                next_id = player.current_room.id

                self.rooms[next_id] = { key: "" for key in player.current_room.get_exits()}

                # print(str(next_id))

                # Map around
                self.rooms[current_id][self.direction] = next_id
                self.rooms[next_id][opposites[self.direction]] = current_id
                visited.add(current_id)
                


        



    # def get_room_paths(self, user_id):
    #     # Because it wants shortest that would be breadth first.
    #     # Extended network tells us it's a traverasal or connected component.

    #     # Planning - How are we going to build the graph? See above, it's already built.
    #     # Start with the given starting_point, do a bft, return the path to each friend.

    #     # Create queue
    #     q = Queue()

    #     # Enqueue path
    #     q.enqueue([user_id])

    #     # Create visited
    #     visited = {}  # Note that this is a dictionary, not a set

    #     # while queue is not empty
    #     while q.size() > 0:

    #         # Dequeue first path
    #         path = q.dequeue()

    #         vertex = path[-1]

    #         # If not visited
    #         if vertex not in visited:

    #             # Do the thing
    #             # What do we need to do?
    #             # Add to visited
    #             visited[vertex] = path

    #             # For each neighbor of vertex
    #             for neighbor in self.connections[vertex]:

    #                 # Copy path and enqueue
    #                 copy_path = path[:]
    #                 copy_path.append(neighbor)
    #                 q.enqueue(copy_path)

    #     return visited



g = Graph()

g.populate_graph()

print("Graph", g.rooms)





# ! --------------------------------------- CODE ENDS HERE 

# TRAVERSAL TEST
# visited_rooms = set()
# player.current_room = world.starting_room
# visited_rooms.add(player.current_room)

# for move in traversal_path:
#     player.travel(move)
#     visited_rooms.add(player.current_room)
#     print("Current room", player.current_room.n_to)

# if len(visited_rooms) == len(room_graph):
#     print(f"TESTS PASSED: {len(traversal_path)} moves, {len(visited_rooms)} rooms visited")
# else:
#     print("TESTS FAILED: INCOMPLETE TRAVERSAL")
#     print(f"{len(room_graph) - len(visited_rooms)} unvisited rooms")



#######
# UNCOMMENT TO WALK AROUND
#######
# player.current_room.print_room_description(player)
# while True:
#     cmds = input("-> ").lower().split(" ")
#     if cmds[0] in ["n", "s", "e", "w"]:
#         player.travel(cmds[0], True)
#     elif cmds[0] == "q":
#         break
#     else:
#         print("I did not understand that command.")
