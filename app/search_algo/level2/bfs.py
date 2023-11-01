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
from app.utils.algo_shared_func import get_neighbors, init_ghost_paths


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
    ghost_paths = init_ghost_paths
    score = 0
    end_node = None

    # Loop until queue is empty
    while queue:
        # Pop the first element from the queue
        node = queue.popleft()
        end_node = node

        # Check if the node is the goal
        if map[node[X]][node[Y]] == FOOD:
            score += 20
            # Backtrack to get the path
            while node != pacman_pos:
                score += 1
                path.append(node)
                node = parent[node]
            path.append(pacman_pos)
            path.reverse()
            # Update score (add 1) for each step (except pacman's starting position)
            if node != pacman_pos:
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
    # get path from pacman to end
    while end_node != pacman_pos:
        path.append(end_node)
        end_node = parent[end_node]
        # Update score (add 1) for each step (except pacman's starting position)
        if end_node != pacman_pos:
            score += 1
    # add pacman's starting position to path
    path.append(pacman_pos)
    score += 1
    path.reverse()

    return path, len(path), ghost_paths, score
