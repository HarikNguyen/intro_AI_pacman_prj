from app.utils.algo_shared_func import get_neighbors, is_food, init_ghost_paths

def dfs(map, map_size, start): 
  frontier = []
  explored = []
  pacman_path = []
  ghost_paths = init_ghost_paths(map)
  # Store how we reached neighbor
  parent_node = {}
  score = 0

  # Add start node
  frontier.append(start)

  while frontier:
    node = frontier.pop()
    explored.append(node)
    if is_food(map, node):
      score += 20
      # Get pacman's path
      while node != start:
        pacman_path.append(node)
        node = parent_node[node]
        # update score upto 1 for each step
        score += 1
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

