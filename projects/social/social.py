import random

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

class User:
    def __init__(self, name):
        self.name = name
    def __repr__(self):
        return self.name


class SocialGraph:
    def __init__(self):
        self.last_id = 0
        self.users = {}
        self.friendships = {}

    def add_friendship(self, user_id, friend_id):
        """
        Creates a bi-directional friendship
        """
        if user_id == friend_id:
            # Refactor
            # print("WARNING: You cannot be friends with yourself")
            return False
        elif friend_id in self.friendships[user_id] or user_id in self.friendships[friend_id]:
            # Refactor
            # print("WARNING: Friendship already exists")
            return False
        else:
            self.friendships[user_id].add(friend_id)
            self.friendships[friend_id].add(user_id)
            return True

    def add_user(self, name):
        """
        Create a new user with a sequential integer ID
        """
        self.last_id += 1  # automatically increment the ID to assign the new user
        self.users[self.last_id] = User(name)
        self.friendships[self.last_id] = set()

    def populate_graph(self, num_users, avg_friendships):
        """
        Takes a number of users and an average number of friendships
        as arguments

        Creates that number of users and a randomly distributed friendships
        between those users.

        The number of users must be greater than the average number of friendships.
        """
        # Reset graph
        self.last_id = 0
        self.users = {}
        self.friendships = {}

        # Add users
        for i in range(0, num_users):
            self.add_user(f"User {i}")

        # New friendship method:
        # Randomly generate friendships, keeping new and rejecting duplicates, until we get to the number we need ( num_users * average friendships // 2)

        # Keep track of good friendships and collisions. Refactor add_friendship
        
        target_friendships = num_users * avg_friendships // 2 # You can either divide this by two or...:87
        total_friendships = 0
        collisions = 0

        while total_friendships < target_friendships:
            user_id = random.randint(1, self.last_id)
            friend_id = random.randint(1, self.last_id)

            if self.add_friendship(user_id, friend_id):
                total_friendships += 1 # Add two here and not divide by two
            else:
                collisions += 1

        print(f"Total collisions: {collisions}")

        # Create Frienships
        # Generate all possible friendship combinations
        # possible_friendships = []

        # Avoid duplicates by ensuring the first number is smaller than the second
        # for user_id in self.users:
        #     for friend_id in range(user_id + 1, self.last_id + 1):
        #         possible_friendships.append((user_id, friend_id))

        # Shuffle the possible friendships
        # random.shuffle(possible_friendships)

        # Create friendships for the first X pairs of the list
        # X is determined by the formula: num_users * avg_friendships // 2
        # Need to divide by 2 since each add_friendship() creates 2 friendships
        # for i in range(num_users * avg_friendships // 2):
        #     friendship = possible_friendships[i]
        #     self.add_friendship(friendship[0], friendship[1])

    def get_all_social_paths(self, user_id):
        """
        Takes a user's user_id as an argument

        Returns a dictionary containing every user in that user's
        extended network with the shortest friendship path between them.

        Shortest is the keyword for a breadth first traversal.

        The key is the friend's ID and the value is the path.
        """
        # !!!! IMPLEMENT ME
        # Because it wants shortest that would be breadth first.
        # Extended network tells us it's a traverasal or connected component.

        # Planning - How are we going to build the graph? See above, it's already built.
        # Start with the given user id, do a bft, return the path to each friend.

        # Create queue
        q = Queue()

        # Enqueue path
        q.enqueue([user_id])

        # Create visited
        visited = {}  # Note that this is a dictionary, not a set

        # while queue is not empty
        while q.size() > 0:

            # Dequeue first path
            path = q.dequeue()

            vertex = path[-1]

            # If not visited
            if vertex not in visited:

                # Do the thing
                # What do we need to do?
                # Add to visited
                visited[vertex] = path

                # For each neighbor of vertex
                for neighbor in self.friendships[vertex]:

                    # Copy path and enqueue
                    copy_path = path[:]
                    copy_path.append(neighbor)
                    q.enqueue(copy_path)

        return visited


if __name__ == '__main__':
    sg = SocialGraph()
    sg.populate_graph(100, 4)
    # print("Friendships")
    # print(sg.friendships)
    connections = sg.get_all_social_paths(1)
    # print("Connections")
    # print(connections)

    total_social_paths = 0
    for user_id in connections:
        total_social_paths += len(connections[user_id])
    print(f"Average length: { total_social_paths / len(connections) }")
