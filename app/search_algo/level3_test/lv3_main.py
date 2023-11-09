from .algo import *

def lv3_main(pacman_pos, map, map_size):
  # Init variables 
  pacman_path_list = []
  ghosts_path_list = init_ghost_paths(map)
  total_score = 0

  while find_entities(map, FOOD):
    # Find foods visible to Pacman
    foods = find_visible_entities(pacman_pos, map, FOOD)
    if foods:
      # Eat nearest food first 
      # Find nearest food using Euclidean heuristic
      foods = sorted(foods, lambda food_pos: heuristic(pacman_pos, food_pos))
      goal = foods[0]
    else:
      goal = random.choice(get_neighbors(map, map_size, pacman_pos))
  
    pacman_path, score = astar_lv3(pacman_pos, map, map_size, goal, ghosts_path_list)
    pacman_path_list.extend(pacman_path)
    total_score += score
    pacman_pos = goal

  return pacman_path_list, len(pacman_path_list), ghosts_path_list, total_score

        
      



