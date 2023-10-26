"""
    Description: Breadth First Search Algorithm for Level 2 (monster is not moving ~ wall)
    BFS: 
        - Start at the root node
        - Explore each neighbour before going to any of their children
        - If the goal node is not found, then it will go back to the root node and repeat the process
        - If the goal node is found, then it will return the path
        - Uses a queue to store the nodes
"""

from collections import deque

from app.constants import WALL, FOOD, X, Y, MONSTER

def bfs(map, map_size, pacman_pos):
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
    queue = deque()
    queue.append(pacman_pos)
    visited = set()
    visited.add(pacman_pos)
    parent = {}
    path = []
    ghost_paths = []
    score = 0

    # Define ghost_paths dict
    for row_id, row in enumerate(map):
        for col_id, _ in enumerate(row):
            ghost_paths.append({"mat_pos": (row_id, col_id), "path": []})

    # Loop until queue is empty
    while queue:
        # Pop the first element from the queue
        node = queue.popleft()

        # Check if the node is the goal
        if map[node[X]][node[Y]] == FOOD:
            # Backtrack to get the path
            while node != pacman_pos:
                path.append(node)
                node = parent[node]
            path.append(pacman_pos)
            path.reverse()
            # Set score = 1
            score += 1
            return path, len(path), ghost_paths, score

        # Get the neighbors of the node
        neighbors = get_neighbors(map, map_size, node)

        # Loop through the neighbors
        for neighbor in neighbors:
            # Check if the neighbor has been visited
            if neighbor not in visited:
                # Add the neighbor to the queue
                queue.append(neighbor)
                visited.add(neighbor)
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
    x = node[X]
    y = node[Y]

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
            if map[neighbor_x][neighbor_y] != WALL and map[neighbor_x][neighbor_y] != MONSTER:
                neighbors.append((neighbor_x, neighbor_y))

    return neighbors