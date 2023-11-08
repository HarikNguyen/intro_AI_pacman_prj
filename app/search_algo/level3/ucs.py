'''
    Description: Search Algorithm for Level 3
'''
from app.settings import BASE_DIR
import random
from app.constants import X, Y, ROAD, WALL, FOOD, MONSTER, INVISIBILITY

# return pacman_path, len(path), ghosts_path, score(status: -2: block; -1: die; 1: success)
def ucs(map, map_size, pacman_pos):
    pacman_res = []
    ghosts_res = []
    scores = []
    score = 0

    food_map = init_food_map(map, map_size)
    count_food = len(find_objects(food_map, map_size, FOOD))
    ghosts = find_objects(map, map_size, MONSTER)

    pacman_map = init_pacman_map(map_size)
    pacman_food_map = init_pacman_food_map(map_size)
    pacman_map = update_pacman_map(map, pacman_map, map_size, pacman_pos)
    pacman_food_map = update_pacman_food_map(food_map, pacman_food_map, map_size, pacman_pos)

    pacman_res.append(pacman_pos)
    ghosts_res.append(ghosts)

    while True:
        if count_food == 0:
            return pacman_res, len(pacman_res), ghosts_res, 1

        if pacman_pos in ghosts:
            return pacman_res, len(pacman_res), ghosts_res, -1

        pacman_path = search_path(pacman_map, pacman_food_map, map_size, pacman_pos)
        
        if len(pacman_path) == 0:
            return pacman_res, len(pacman_res), ghosts_res, -2
        
        if check_safe_move(pacman_map, map_size, pacman_path[1]):
            pacman_pos = pacman_path[1]
        else:
            pacman_pos = change_path(pacman_map, map_size, pacman_pos)
        
        ghosts = get_ghosts_move(map, map_size, ghosts)
        pacman_res.append(pacman_pos)
        ghosts_res.append(ghosts)
        score -= 1

        map = update_map(map, map_size, ghosts)
        pacman_map = update_pacman_map(map, pacman_map, map_size, pacman_pos)
        pacman_food_map = update_pacman_food_map(food_map, pacman_food_map, map_size, pacman_pos)

        if food_map[pacman_pos[X]][pacman_pos[Y]] == FOOD:
            food_map[pacman_pos[X]][pacman_pos[Y]] = 0
            pacman_food_map[pacman_pos[X]][pacman_pos[Y]] = 0
            count_food -= 1
            score += 20
        
        scores.append(score)


def change_path(pacman_map, map_size, pacman_pos):
    neighbors = get_neighbors(pacman_map, map_size, pacman_pos)
    safe_pos = []
    for neighbor in neighbors:
        if check_safe_move(pacman_map, map_size, neighbor):
            safe_pos.append(neighbor)
    if len(safe_pos) == 0:
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        for dir in directions:
            new_pos_x = pacman_pos[X] + dir[X]
            new_pos_y = pacman_pos[Y] + dir[Y]
            if pacman_map[new_pos_x][new_pos_y] != WALL:
                return (new_pos_x, new_pos_y)
    return random.choice(safe_pos)


def search_path(pacman_map, pacman_food_map, map_size, pacman_pos):
    path = []
    foods = find_objects(pacman_food_map, map_size, FOOD)
    foods.sort(key = lambda food: heuristic(pacman_pos, food))
    while foods:
        path = a_star(pacman_map, map_size, pacman_pos, foods[0])
        if len(path) != 0:
            return path
        foods.pop(0)
    
    invisibility = find_objects(pacman_map, map_size, INVISIBILITY)
    invisibility.sort(key = lambda inv: heuristic(pacman_pos, inv))
    # print(invisibility)
    while invisibility:
        path = a_star(pacman_map, map_size, pacman_pos, invisibility[0])
        if len(path) != 0:
            return path
        invisibility.pop(0)
    
    return path # empty array path


def a_star(pacman_map, map_size, pacman_pos, goal):
    queue = [(0, pacman_pos)] # (cost, position)
    visited = set()
    parent = {}
    path = []

    while queue:
        cost, current_node = queue.pop(0)

        if current_node == goal:
            while current_node != pacman_pos:
                path.append(current_node)
                current_node = parent[current_node]
            path.append(pacman_pos)
            path.reverse()
            return path
        
        if current_node not in visited:
            visited.add(current_node)
            for neighbor in get_neighbors(pacman_map, map_size, current_node):
                if neighbor not in visited:
                    parent[neighbor] = current_node
                    queue.append((cost + 1, neighbor))
            queue.sort(key=lambda x: x[0] + heuristic(x[1], goal))
    return path


def heuristic(node, goal):
    return abs(goal[X] - node[X]) + abs(goal[Y] - node[Y])


def find_objects(map, map_size, obj):
    result = []
    for row in range(map_size[X]):
        for col in range(map_size[Y]):
            if map[row][col] == obj:
                result.append((row, col))
    return result


def get_neighbors(map, map_size, node):
    neighbors = []

    # Define the directions (top - left - bottom - right)
    directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]

    for direction in directions:
        neighbor_x = node[X] + direction[X]
        neighbor_y = node[Y] + direction[Y]
        
        if 0 <= neighbor_x < map_size[X] and 0 <= neighbor_y <map_size[Y]:
            if map[neighbor_x][neighbor_y] != WALL:# and map[neighbor_x][neighbor_y] != MONSTER:# and map[neighbor_x][neighbor_y] != INVISIBILITY:
                neighbors.append((neighbor_x, neighbor_y))
    
    return neighbors


def init_food_map(map, map_size):
    food_map = [[0 for _ in range(map_size[Y])] for _ in range(map_size[X])]
    for x in range(map_size[X]):
        for y in range(map_size[Y]):
            if map[x][y] == FOOD:
                food_map[x][y] = FOOD
    return food_map


def init_pacman_food_map(map_size):
    pacman_food_map = [[0 for _ in range(map_size[Y])] for _ in range(map_size[X])]
    return pacman_food_map


def update_pacman_food_map(food_map, pacman_food_map, map_size, pacman_pos):
    for x in range(map_size[X]):
        for y in range(map_size[Y]):
            if abs(x - pacman_pos[X]) <= 3 and abs(y - pacman_pos[Y]) <= 3:
                if food_map[x][y] == FOOD:
                    pacman_food_map[x][y] = FOOD
    return pacman_food_map


def init_pacman_map(map_size):
    pacman_map = [[INVISIBILITY for _ in range(map_size[Y])] for _ in range(map_size[X])]
    return pacman_map


def update_pacman_map(map, pacman_map, map_size, pacman_pos):
    for x in range(map_size[X]):
        for y in range(map_size[Y]):
            if abs(x - pacman_pos[X]) <= 3 and abs(y - pacman_pos[Y]) <= 3:
                if map[x][y] == FOOD:
                    pacman_map[x][y] = ROAD
                else:
                    pacman_map[x][y] = map[x][y]
    
    for x in range(map_size[X]):
        for y in range(map_size[Y]):
            if abs(x - pacman_pos[X]) > 3 and abs(y - pacman_pos[Y]) > 3:
                if pacman_map[x][y] == MONSTER:
                    pacman_map[x][y] = ROAD

    return pacman_map


def get_ghost_neighbor(map, map_size, node):
    neighbors = []

    directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    
    for direction in directions:
        neighbor_x = node[X] + direction[X]
        neighbor_y = node[Y] + direction[Y]

        if 0 <= neighbor_x < map_size[X] and 0 <= neighbor_y < map_size[Y]:
            if map[neighbor_x][neighbor_y] != WALL:
                neighbors.append((neighbor_x, neighbor_y))
    
    return neighbors


def get_ghosts_move(map, map_size, ghosts):
    ghosts_pos = []

    for ghost in ghosts:
        ghost_neighbors = get_ghost_neighbor(map, map_size, ghost)

        if len(ghost_neighbors) == 0:
            new_pos = ghost
        else:
            new_pos = random.choice(ghost_neighbors)
        
        ghosts_pos.append(new_pos)
    return ghosts_pos


def update_map(map, map_size, ghosts):
    for x in range(map_size[X]):
        for y in range(map_size[Y]):
            if map[x][y] == MONSTER:
                map[x][y] = ROAD
    
    for ghost in ghosts:
        map[ghost[X]][ghost[Y]] = MONSTER
    
    return map


def check_safe_move(pacman_map, map_size, move_pos):
    ghosts = find_objects(pacman_map, map_size, MONSTER)
    for ghost in ghosts:
        if heuristic(move_pos, ghost) <= 1:
            return False
    return True