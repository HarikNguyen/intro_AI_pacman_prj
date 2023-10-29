from collections import deque
def is_food(map, pos):
  return map[pos[0]][pos[1]] == 2

def is_wall(map, pos):
  return map[pos[0]][pos[1]] == 1

def is_monster(map, pos):
  return map[pos[0]][pos[1]] == 3

def is_in_map(map_size, pos):
  return 0 <= pos[0] < map_size[0] and 0 <= pos[1] < map_size[1]

def is_explored_node(explored, node):
  return node in explored

def get_neighbors(map, map_size, node):
    """Get the neighbors of the node
    neighbors are the nodes that are adjacent to the node, excluding the blocked nodes (walls/monsters)

    Args:
        map: 2D array of integers
        node: tuple of integers (node's position)
    """

    # Initialize variables
    neighbors = []
    x = node[0]
    y = node[1]

    # Define the directions (top - bottom - left - right)
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    # Loop through the directions
    for direction in directions:
        # Get the neighbor's position
        neighbor_x = x + direction[0]
        neighbor_y = y + direction[1]

        # Check if the neighbor is within the map, not a wall and not a monster
        if (
           is_in_map(map_size, (neighbor_x, neighbor_y)) 
           and not is_wall(map, (neighbor_x, neighbor_y)) 
           and not is_monster(map, (neighbor_x, neighbor_y))
        ):
          neighbors.append((neighbor_x, neighbor_y))

    return neighbors



def dfs(map, map_size, start): 
  frontier = []
  explored = []
  pacman_path = []
  # Store how we reached neighbor
  parent_node = {}
  score = 0

  # Add start node
  frontier.append(start)

  while frontier:
    node = frontier.pop()
    explored.append(node)
    score += 1
    if is_food(map, node):
      score += 20
      # Get pacman's path
      while node != start:
        pacman_path.append(node)
        node = parent_node[node]
      pacman_path.append(start)
      pacman_path.reverse()
      break

    neighbors = get_neighbors(map, map_size, node)
    if neighbors:
      # Add nodes that are not explored
      for neighbor in neighbors:
        if neighbor not in explored:
          frontier.append(neighbor) 
          parent_node[neighbor] = node
  
  return pacman_path, len(pacman_path), [], score

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
        if map[node[0]][node[1]] == 2:
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
    x = node[0]
    y = node[1]

    # Define the directions (top - bottom - left - right)
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    # Loop through the directions
    for direction in directions:
        # Get the neighbor's position
        neighbor_x = x + direction[0]
        neighbor_y = y + direction[1]

        # Check if the neighbor is within the map
        if 0 <= neighbor_x < map_size[0] and 0 <= neighbor_y < map_size[1]:
            # Check if the neighbor is not a wall
            if map[neighbor_x][neighbor_y] != 1:
                neighbors.append((neighbor_x, neighbor_y))

    return neighbors

map = [[1, 1, 1, 1, 1],[1, 0, 0, 0, 1], [2, 0, 1, 0, 1], [1, 0, 1, 0, 0], [1, 1, 1, 1, 1]]
path, path_len, ghost_path, score = bfs(map, (5,5), (3,4))
print(path)