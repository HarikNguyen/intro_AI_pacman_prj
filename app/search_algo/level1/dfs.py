from app.utils.algo_shared_func import is_food, get_neighbors, init_ghost_paths

def dfs(map, map_size, start): 
  frontier = [] # stack
  explored = []
  pacman_path = []
  # Store how we reached neighbor
  parent_node = {}
  ghost_paths = init_ghost_paths(map)
  score = 0
  end_node = None

  # Add start node
  frontier.append(start)

  while frontier:
    node = frontier.pop()
    end_node = node
    explored.append(node)

    if is_food(map, node):
      score += 20
      # Get pacman's path
      while node != start:
        pacman_path.append(node)
        node = parent_node[node]
        score += 1
      pacman_path.append(start)
      pacman_path.reverse()
      return pacman_path, len(pacman_path), ghost_paths, score

    neighbors = get_neighbors(map, map_size, node)
    if neighbors:
      # Add nodes that are not explored
      for neighbor in neighbors:
        if neighbor not in explored:
          frontier.append(neighbor) 
          parent_node[neighbor] = node
  
  return pacman_path, len(pacman_path), [], score

