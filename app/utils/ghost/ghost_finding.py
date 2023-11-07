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
    init_ghost_paths,
)
from random import randint


def get_ghost_paths(map, map_size, cur_pacman_pos):
    ghost_paths = init_ghost_paths(map)

    for row_id, row in enumerate(map):
        for col_id, cell in enumerate(row):
            if is_monster(map, (row_id, col_id)):
                ghost_paths[(row_id, col_id)] = ghost_finding(
                    map, map_size, (row_id, col_id), cur_pacman_pos
                )

    return ghost_paths


def ghost_finding(map, map_size, cur_ghost_pos, cur_pacman_pos):
    # A* algorithm with heuristic is manhattan distance
    # And goal is one of blocking points if it is effective or pacman position

    # Find blocking points
    blocking_points = find_blocking_points(map, map_size, cur_pacman_pos)

    goal = (
        blocking_points[randint(0, len(blocking_points) - 1)]
        if len(blocking_points) > 0
        else cur_pacman_pos
    )

    return a_star_search(map, map_size, cur_ghost_pos, goal)


def a_star_search(map, map_size, start, goal):
    # Initialize variables
    frontier = []
    explored = []
    path = []
    cost = 0

    # Add start node to frontier
    frontier.append((start, cost))

    # Loop until frontier is empty
    while len(frontier) > 0:
        # Get the node with the lowest cost
        frontier.sort(key=lambda x: x[1])
        node = frontier.pop(0)

        # Check if the node is the goal
        if node[0] == goal:
            # Get the path
            path = get_path(explored, node)

            # Return the path
            return path

        # Add the node to the explored list
        explored.append(node[0])

        # Get the neighbors of the node
        neighbors = get_neighbors(map, map_size, node[0])

        # Loop through the neighbors
        for neighbor in neighbors:
            # Check if the neighbor has been explored
            if not is_explored_node(explored, neighbor):
                # Calculate the cost of the neighbor
                cost = node[1] + 1 + heuristic(neighbor, goal)

                # Add the neighbor to the frontier
                frontier.append


def heuristic(start, goal):
    return abs(start[X] - goal[X]) + abs(start[Y] - goal[Y])


def get_path(explored, node):
    path = []

    # Loop until the node is None
    while node != None:
        # Add the node to the path
        path.append(node[0])

        # Get the parent of the node
        node = get_parent(explored, node)

    # Reverse the path
    path.reverse()

    # Return the path
    return path


def get_parent(explored, node):
    # Loop through the explored nodes
    for explored_node in explored:
        # Check if the explored node is the parent of the node
        if explored_node[0] == node[2]:
            return explored_node

    return None


def is_explored_node(explored, node):
    # Loop through the explored nodes
    for explored_node in explored:
        # Check if the explored node is the same as the node
        if explored_node[0] == node:
            return True

    return False


def find_blocking_points(map, map_size, cur_pacman_pos):
    blocking_points = []

    # Loop through all points in map
    for row_id, row in enumerate(map):
        for col_id, cell in enumerate(row):
            if is_blocking_point(map, map_size, (row_id, col_id)):
                blocking_points.append((row_id, col_id))

    # Remove ineffective blocking points
    for blocking_point in blocking_points:
        if not is_effective_blocking_point(
            map, map_size, cur_pacman_pos, blocking_point
        ):
            blocking_points.remove(blocking_point)

    return blocking_points


def is_blocking_point(map, map_size, point):
    """Check if a point is a blocking point or not

    Args:
        map (list of list int): map matrix
        map_size (tuple of int): map size
        point (tuple of int): point to check

    Return:
        True if point is a blocking point, False otherwise
    """

    for direction in DIRECTION_VECTOR.values():
        near_pos = (point[X] + direction[X], point[Y] + direction[Y])
        if (
            not is_in_map(map_size, near_pos)
            or is_wall(map, near_pos)
            or is_monster(map, near_pos)
        ):
            return True

    return False


def is_effective_blocking_point(cur_pacman_pos, blocking_point):
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

    if manhattan_distance >= 3:
        return True

    return False
