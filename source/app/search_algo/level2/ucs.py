"""
    Description: Breadth First Search Algorithm for Level 1
    BFS: 
        - Start at the root node
        - Explore each neighbour before going to any of their children
        - If the goal node is not found, then it will go back to the root node and repeat the process
        - If the goal node is found, then it will return the path
        - Uses a queue to store the nodes
"""

from app.constants import WALL, FOOD, X, Y, MONSTER, EAT_FOOD_SCORE, MOVE_SCORE
from app.utils.algo_shared_func import init_ghost_paths


def ucs(map, map_size, pacman_pos):
    """
    Description: Breadth First Search Algorithm for Level 1
    Input:
        - map: 2D array of integers
        - start: tuple of integers (pacman's starting position)
        - pacman_pos: tuple of integers (food's position)
    Output:
        - finding_path: list of tuples
            - finding_path_length: integer
        - score: integer
    """
    # Initialize variables
    frontier = []
    frontier.append((0, pacman_pos))
    explored = set()
    parent = dict()
    path = []
    ghost_paths = init_ghost_paths(map)
    score = 0

    # Define ghost_paths dict
    for row_id, row in enumerate(map):
        for col_id, cell in enumerate(row):
            if cell == MONSTER:
                ghost_paths.append({"mat_pos": (row_id, col_id), "path": []})

    # Loop until queue is empty
    while frontier:
        # Pop the first element from the queue
        node = frontier.pop(0)

        # Check if the node is the goal
        if map[node[1][X]][node[1][Y]] == FOOD:
            # Update score upto EAT_FOOD_SCORE for each food
            score += EAT_FOOD_SCORE
            # Backtrack to get the path
            while node[1] != pacman_pos:
                path.append(node[1])
                node = parent[node]
                # update score upto MOVE_SCORE for each step
                score += MOVE_SCORE
            path.append(pacman_pos)
            path.reverse()
            return path, len(path), ghost_paths, score

        explored.add(node[1])
        # Get the neighbors of the node
        neighbors = get_neighbors(map, map_size, node)

        # Loop through the neighbors
        for neighbor in neighbors:
            # Check if the neighbor has been explored and neighbor is monster
            if (
                neighbor[1] not in explored
                and map[neighbor[1][0]][neighbor[1][1]] != MONSTER
            ):
                index = searchPosInFrontier(neighbor[1], frontier)
                if index == -1:
                    insertIntoFrontier(neighbor, frontier)
                    parent[neighbor] = node
                elif frontier[index][0] > neighbor[0]:
                    frontier.pop(index)
                    insertIntoFrontier(neighbor, frontier)
                    parent[neighbor] = node

    # if all nodes in frontier (queue) are visited and the goal is not found (score = 0)
    return path, len(path), ghost_paths, score


def get_neighbors(map, map_size, node):
    """Get the neighbors of the node
    neighbors are the nodes that are adjacent to the node, excluding the blocked nodes (walls/monsters)

    Args:
        map: 2D array of integers
        node: tuple of integers (node's position)
    """

    # Initialize variables
    neighbors = []
    x = node[1][X]
    y = node[1][Y]
    cost = node[0]

    # Define the directions (top - bottom - left - right)
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    # Loop through the directions
    for direction in directions:
        # Get the neighbor's position
        neighbor_x = x + direction[X]
        neighbor_y = y + direction[Y]

        # Check if the neighbor is within the map
        if 0 <= neighbor_x < map_size[X] and 0 <= neighbor_y < map_size[Y]:
            # Check if the neighbor is not a wall
            if map[neighbor_x][neighbor_y] != WALL:
                neighbors.append((cost + 1, (neighbor_x, neighbor_y)))

    return neighbors


# Return index of position in frontier
def searchPosInFrontier(pos, frontier):
    for i in range(len(frontier)):
        if frontier[i][1] == pos:
            return i
    return -1


# Insert item into frontier base on item cost
def insertIntoFrontier(node, frontier):
    for i in range(len(frontier)):
        if node[0] < frontier[i][0]:
            frontier.insert(i, node)
            return
    frontier.append(node)
