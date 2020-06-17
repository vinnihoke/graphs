from room import Room
from player import Player
from world import World

import random
from ast import literal_eval
import time

# Load world
world = World()


# You may uncomment the smaller graphs for development and testing purposes.

# map_file = "maps/test_line.txt"
map_file = "maps/test_cross.txt"
# map_file = "maps/test_loop.txt"
# map_file = "maps/test_loop_fork.txt"
# map_file = "maps/main_maze.txt"

# Loads the map into a dictionary
room_graph = literal_eval(open(map_file, "r").read())
world.load_graph(room_graph)

# Print an ASCII map
world.print_rooms()

player = Player(world.starting_room)

# ! ------------------------------------- CODE STARTS HERE
# Goal is to create a traversal path array of direction strings that traverses the entire map.
opposites = {
    'n': 's',
    's': 'n',
    'w': 'e',
    'e': 'w'
}


def traverse(starting_room, visited=None, path=None):
    time.sleep(4)

    # Initialize visited and path
    if visited is None:
        visited = set()
    if path is None:
        path = []

    # Add the room to visited
    visited.add(starting_room)

    # Add the room to path
    path = path + [starting_room]

    # For each move in the current room exits
    for move in player.current_room.get_exits():

        # Move in that direction
        player.travel(move)

        # Record that room
        new_room = player.current_room

        # If we haven't been there before
        if new_room not in visited:

            # Add the new room to visited
            visited.add(new_room)

            # Add the move to the path
            path.append(move)

            # Add to the path by recursion until it gets stuck.
            path = path + traverse(new_room, visited)

            # Reverse travel direction and go back to start
            player.travel(opposites[move])

            # Add the direction to the path
            path.append(opposites[move])

            print("Current Room: ", player.current_room.id)

        # We have been there before
        else:

            # Leave the room in the opposite direction
            player.travel(opposites[move])

    # Return traversal path
    return path

traversal_path = traverse(player.current_room)

# ! --------------------------------------- CODE ENDS HERE

# TRAVERSAL TEST
visited_rooms = set()
player.current_room = world.starting_room
visited_rooms.add(player.current_room)

for move in traversal_path:
    player.travel(move)
    visited_rooms.add(player.current_room)
    print("Current room", player.current_room.n_to)

if len(visited_rooms) == len(room_graph):
    print(f"TESTS PASSED: {len(traversal_path)} moves, {len(visited_rooms)} rooms visited")
else:
    print("TESTS FAILED: INCOMPLETE TRAVERSAL")
    print(f"{len(room_graph) - len(visited_rooms)} unvisited rooms")


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
