import heapq
import random
from app.constants import WALL, ROAD, FOOD, X, Y, MONSTER, EAT_FOOD_SCORE, MOVE_SCORE
from app.utils.algo_shared_func import *

# Return lists of entities visible to Pacman (in 7x7 square)
# def find_visible_entities(pacman_pos, map, entity):
#   visible_entities = []
#   for i in range(pacman_pos[X] - 3, pacman_pos[X] + 3):
#     for j in range(pacman_pos[Y] - 3, pacman_pos[Y] + 3):
#       if map[i][j] == entity:
#         visible_entities.append((i, j))
#   return visible_entities

def find_visible_entities(pacman_pos, map, entity):
  visible_entities = []
  for i in range(pacman_pos[X] - 3, pacman_pos[X] + 4):  # Adjust the range to include the center
    for j in range(pacman_pos[Y] - 3, pacman_pos[Y] + 4):  # Adjust the range to include the center
      if 0 <= i < len(map) and 0 <= j < len(map[0]) and map[i][j] == entity:
        visible_entities.append((i, j))
  return visible_entities

def find_entities(map, entity):
  entities = []
  for i in range(len(map)):
    for j in range(len(map[i])):
      if map[i][j] == entity:
        entities.append((i, j))
  return entities

# Define heuristic function: Euclidean Heuristic
# This function is used for estimating the cost to reach the goal from the node
def heuristic(node, goal):
  return ((node[X] - goal[X])**2 + (node[Y] - goal[Y])**2) ** 0.5

# Find neighbors of current node with its f_cost
# item = (f_cost, current node)
def get_neighbors_with_fcost(map, map_size, item, goal):
    # Init variables
    neighbors = []
    f_cost, node = item
    x = node[X]
    y = node[Y]

    # Define the directions (top - bottom - left - right)
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    # Loop through the directions
    for direction in directions:
        # Get the neighbor's position
        neighbor_x = x + direction[X]
        neighbor_y = y + direction[Y]

        # Check if the neighbor is within the map, not a wall and not a monster
        if (
           is_in_map(map_size, (neighbor_x, neighbor_y)) 
           and not is_wall(map, (neighbor_x, neighbor_y)) 
           and not is_monster(map, (neighbor_x, neighbor_y))
        ):
          f_cost = 1 + heuristic((neighbor_x, neighbor_y), goal)
          neighbors.append((f_cost, (neighbor_x, neighbor_y)))

    return neighbors

# A* algorithm for level 3
def astar_lv3(start, map, map_size, goal, ghost_paths):
  pacman_path = []
  score = 0

  # Init variables for A* algorithm
  g_cost = 0 # Start has 0 g_cost
  h_cost = heuristic(start, goal)
  f_cost = g_cost + h_cost 
  frontier = [] # Priority queue
  explored = set()
  parent = {} # Store how we reached neighbor

  # Add start to priority queue
  heapq.heappush(frontier, (f_cost, start))
  while frontier:
    item = heapq.heappop(frontier)
    f_cost, node = item

    # Check if node is the goal
    if is_goal(node, goal):
      # Update score upto EAT_FOOD_SCORE for each step
      score += EAT_FOOD_SCORE
      # Get Pacman's path
      while node != start:
        pacman_path.append(node)
        node = parent[node]
        # Update score upto MOVE_SCORE for each step
        score += MOVE_SCORE
      pacman_path.append(start)
      pacman_path.reverse()
      break
    
    # Move ghosts after Pac-Man's movement
    move_ghosts(ghost_paths, map, map_size)
    
    explored.add(item)
    # Find neighbors of current node
    neighbors = get_neighbors_with_fcost(map, map_size, item, goal)
    if neighbors:
      for neighbor in neighbors:
        if neighbor not in explored:
          heapq.heappush(frontier, neighbor)
          parent[neighbor[1]] = node

  return pacman_path, score

def move_ghosts(ghost_paths, map, map_size):
  for ghost_path in ghost_paths:
    # Ghost's current possition
    ghost_pos = ghost_path['mat_pos']
    ghost_path['path'].append(ghost_pos)
    # Choose new position 
    new_ghost_pos = random.choice(get_neighbors(map, map_size, ghost_pos))
    ghost_path['mat_pos'] = new_ghost_pos
    ghost_path['path'].append(new_ghost_pos)
    # Update map
    map[new_ghost_pos[X]][new_ghost_pos[Y]] = MONSTER
    map[ghost_pos[X]][ghost_pos[Y]] = ROAD





