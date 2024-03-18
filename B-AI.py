# a Python program that implements a simple version of the 
# A* algorithm, a popular pathfinding algorithm used in artificial intelligence and robotics:



import heapq

class Node:
    def __init__(self, state, parent=None, action=None, g_cost=0, h_cost=0):
        self.state = state
        self.parent = parent
        self.action = action
        self.g_cost = g_cost  # cost from start node to current node
        self.h_cost = h_cost  # heuristic cost from current node to goal node

    def __lt__(self, other):
        return (self.g_cost + self.h_cost) < (other.g_cost + other.h_cost)

class AStar:
    def __init__(self, start_state, goal_state, get_neighbors_fn, heuristic_fn):
        self.start_state = start_state
        self.goal_state = goal_state
        self.get_neighbors_fn = get_neighbors_fn
        self.heuristic_fn = heuristic_fn

    def find_path(self):
        open_set = []
        closed_set = set()

        start_node = Node(self.start_state)
        heapq.heappush(open_set, start_node)

        while open_set:
            current_node = heapq.heappop(open_set)

            if current_node.state == self.goal_state:
                return self.construct_path(current_node)

            closed_set.add(current_node.state)

            for action, neighbor_state, cost in self.get_neighbors_fn(current_node.state):
                if neighbor_state in closed_set:
                    continue

                g_cost = current_node.g_cost + cost
                h_cost = self.heuristic_fn(neighbor_state, self.goal_state)
                neighbor_node = Node(neighbor_state, current_node, action, g_cost, h_cost)

                heapq.heappush(open_set, neighbor_node)

        return None  # Path not found

    def construct_path(self, node):
        path = []
        while node:
            path.append((node.action, node.state))
            node = node.parent
        return list(reversed(path))

# Example usage
def get_neighbors(state):
    neighbors = [
        ('up', (state[0] - 1, state[1]), 1),
        ('down', (state[0] + 1, state[1]), 1),
        ('left', (state[0], state[1] - 1), 1),
        ('right', (state[0], state[1] + 1), 1)
    ]
    return [(action, neighbor, cost) for action, neighbor, cost in neighbors if 0 <= neighbor[0] < 5 and 0 <= neighbor[1] < 5]

def manhattan_distance(state, goal_state):
    return abs(state[0] - goal_state[0]) + abs(state[1] - goal_state[1])

start_state = (0, 0)
goal_state = (4, 4)
astar = AStar(start_state, goal_state, get_neighbors, manhattan_distance)
path = astar.find_path()
print("Path:", path)


# This program finds a path from a start state to a goal state on a grid using the AI algorithm. 
# You can customize the grid size, start state, and goal state, as well as the heuristic function and neighbor generation function. 
# This implementation demonstrates proficiency in algorithmic thinking, object-oriented programming, and problem-solving skills.















