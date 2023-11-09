# Ghost finding will catch the pacman and eat it.

# Target catch pacman by shortest path, trap it in a corner and eat it.
# To catch and trap pacman, ghost need to know where position block pacman movement.
# A blocking point is a point that is surrounded by walls, other ghosts, and dead ends

from app.constants import DIRECTION_VECTOR, X, Y
from app.utils.algo_shared_func import (
    is_in_map,
    is_wall,
    is_monster,
    get_neighbors,
    is_road_for_ghost,
)
from math import sqrt
from random import randint


def get_ghost_paths(map, map_size, cur_pacman_pos, cur_ghosts_pos):
    ghost_paths = []

    for cur_ghost_pos in cur_ghosts_pos:
        finding_path = ghost_finding(map, map_size, cur_ghost_pos, cur_pacman_pos)
        if len(finding_path) > 1:
            ghost_paths.append(finding_path[1])
        elif len(finding_path) == 1:
            ghost_paths.append(finding_path[0])
        else:
            neighbors_ghost = get_neighbors(map, map_size, cur_ghost_pos)
            ghost_paths.append(neighbors_ghost[randint(0, len(neighbors_ghost) - 1)])

    return ghost_paths


def ghost_finding(map, map_size, cur_ghost_pos, cur_pacman_pos):
    # A* algorithm with heuristic is manhattan distance
    # And goal is one of blocking points if it is effective or pacman position

    # Find blocking points
    blocking_points = find_blocking_points(map, map_size, cur_pacman_pos)
    # Find path
    goal = cur_pacman_pos
    path_found = []
    while True:
        if len(blocking_points) > 0:
            rand_index = randint(0, len(blocking_points) - 1)
            goal = blocking_points[rand_index]
            # pop blocking point in blocking_points
            path_found = a_star_search(map, map_size, cur_ghost_pos, goal)
            blocking_points.pop(rand_index)
            if len(path_found) > 0:
                break
        else:
            goal = cur_pacman_pos
            path_found = a_star_search(map, map_size, cur_ghost_pos, goal)
            break
    return path_found


POINT_ID = 0
COST_ID = 1


def a_star_search(map, map_size, start, goal):
    # Initialize variables
    frontier = []
    explored = []
    path = []
    parents = {}
    cost = 0

    # Add start node to frontier
    frontier.append((start, cost))

    # Loop until frontier is empty
    while len(frontier) > 0:
        # Get the node with the lowest cost
        frontier.sort(key=lambda x: x[1])
        node = frontier.pop(0)
        # Check if the node is the goal
        if node[POINT_ID] == goal:
            # Get the path
            path = get_path(parents, node[POINT_ID])

            # Return the path
            return path

        # Add the node to the explored list
        explored.append(node[POINT_ID])

        # Get the neighbors of the node
        neighbors = get_ghost_neighbors(map, map_size, node[POINT_ID])
        # Loop through the neighbors
        for neighbor in neighbors:
            # Check if the neighbor has been explored
            if neighbor not in explored:
                # Calculate the cost of the neighbor
                cost = node[COST_ID] + 1 + heuristic(neighbor, goal)

                # Add the neighbor to the frontier
                frontier.append((neighbor, cost))

                # Add the neighbor to the parents list
                parents[neighbor] = node[POINT_ID]

    return path


def get_ghost_neighbors(map, map_size, ghost_pos):
    neighbors = []
    for direction in DIRECTION_VECTOR.values():
        near_pos = (ghost_pos[X] + direction[X], ghost_pos[Y] + direction[Y])
        if is_in_map(map_size, near_pos) and is_road_for_ghost(map, near_pos):
            neighbors.append(near_pos)
    return neighbors


def get_path(parents, node):
    path = []

    # Loop until there is no parent
    while node is not None:
        # Add the node to the path
        path.append(node)

        # Get the parent of the node
        node = parents.get(node, None)

    # Reverse the path
    path.reverse()

    return path


def heuristic(start, goal):
    # return abs(start[X] - goal[X]) + abs(start[Y] - goal[Y])
    euclidean_distance = ((start[X] - goal[X]) ** 2 + (start[Y] - goal[Y]) ** 2) ** 0.5
    return sqrt(euclidean_distance)


def find_blocking_points(map, map_size, cur_pacman_pos):
    blocking_points = []

    # Loop through all points in map
    for row_id, row in enumerate(map):
        for col_id, cell in enumerate(row):
            if is_blocking_point(map, map_size, (row_id, col_id)):
                blocking_points.append((row_id, col_id))

    # Remove ineffective blocking points
    effective_blocking_points = []
    for blocking_point in blocking_points:
        if is_effective_blocking_point(map, map_size, cur_pacman_pos, blocking_point):
            effective_blocking_points.append(blocking_point)

    return effective_blocking_points


def is_blocking_point(map, map_size, point):
    """Check if a point is a blocking point or not

    Args:
        map (list of list int): map matrix
        map_size (tuple of int): map size
        point (tuple of int): point to check

    Return:
        True if point is a blocking point, False otherwise
    """

    if not is_road_for_ghost(map, point):
        return False

    for direction in DIRECTION_VECTOR.values():
        near_pos = (point[X] + direction[X], point[Y] + direction[Y])
        if (
            not is_in_map(map_size, near_pos)
            or is_wall(map, near_pos)
            or is_monster(map, near_pos)
        ):
            return True

    return False


def is_effective_blocking_point(map, map_size, cur_pacman_pos, blocking_point):
    """Check if a blocking point is effective for trapping pacman or not
    It effective if it far away from pacman at least a threshold (cell). Threshold = 3

    Args:
        map (list of list int): map matrix
        map_size (tuple of int): map size
        cur_pacman_pos (tuple of int): current pacman position
        blocking_point (tuple of int): blocking point to check

    Return:
        True if blocking point is effective for trap pacman, False otherwise
    """

    manhattan_distance = abs(cur_pacman_pos[X] - blocking_point[X]) + abs(
        cur_pacman_pos[Y] - blocking_point[Y]
    )
    if manhattan_distance <= 2:
        return True

    return False
