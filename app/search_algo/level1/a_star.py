import heapq

# Constants for map elements
EMPTY = 0
WALL = 1
FOOD = 2
MONSTER = 3

# Scoring constants
MOVE_SCORE = 1  # Score for each move
EAT_FOOD_SCORE = 20  # Score for eating food

# A* search algorithm to find a path from 'pacman_pos' to 'food_pos' in the 'map' of size 'map_size'
def a_star(map, map_size, pacman_pos):
    rows, cols = map_size
    distance = [[float("inf") for _ in range(cols)] for _ in range(rows)]
    parent = [[None for _ in range(cols)] for _ in range(rows)]

    distance[pacman_pos[0]][pacman_pos[1]] = 0

    min_heap = [(0, pacman_pos)]
    food_positions = [
        (r, c) for r in range(rows) for c in range(cols) if map[r][c] == FOOD
    ]
    ghost_positions = [
        (r, c) for r in range(rows) for c in range(cols) if map[r][c] == MONSTER
    ]

    while min_heap:
        dist, current = heapq.heappop(min_heap)

        if current in food_positions:
            path = []
            while current:
                path.append(current)
                current = parent[current[0]][current[1]]

            path = list(reversed(path))  # Reverse the path

            # Calculate the score based on the number of steps (moves) and food eaten
            num_moves = len(path) - 1  # Subtract 1 for the initial position
            score = num_moves * MOVE_SCORE + len(food_positions) * EAT_FOOD_SCORE

            # Update ghost paths
            ghost_paths = []
            for ghost_pos in ghost_positions:
                ghost_path = []
                while ghost_pos:
                    ghost_path.append(ghost_pos)
                    ghost_pos = parent[ghost_pos[0]][ghost_pos[1]]
                ghost_path = list(reversed(ghost_path))
                ghost_paths.append(ghost_path)

            return path, num_moves, ghost_paths, score

        if dist > distance[current[0]][current[1]]:
            continue

        for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            new_r, new_c = current[0] + dr, current[1] + dc

            if 0 <= new_r < rows and 0 <= new_c < cols and map[new_r][new_c] != WALL:
                new_dist = dist + 1

                if new_dist < distance[new_r][new_c]:
                    distance[new_r][new_c] = new_dist
                    parent[new_r][new_c] = current
                    heapq.heappush(min_heap, (new_dist, (new_r, new_c)))

    return [], 0, [], 0
