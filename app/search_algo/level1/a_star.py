import heapq

# Constants for map elements
EMPTY = 0
WALL = 1
FOOD = 2
MONSTER = 3

# A* search algorithm to find a path from 'pacman_pos' to 'food_pos' in the 'map' of size 'map_size'
def a_star(map, map_size, pacman_pos):
    rows, cols = map_size  # Get the map size
    distance = [[float('inf') for _ in range(cols)] for _ in range(rows)]  # Initialize distances to infinity
    parent = [[None for _ in range(cols)] for _ in range(rows)]  # Initialize parent pointers

    distance[pacman_pos[0]][pacman_pos[1]] = 0  # Pac-Man's position has a distance of 0

    min_heap = [(0, pacman_pos)]  # Priority queue to keep track of nodes to explore

    food_positions = [(r, c) for r in range(rows) for c in range(cols) if map[r][c] == FOOD]
    ghost_paths = [{"mat_pos": (r, c), "path": []} for r in range(rows) for c in range(cols) if map[r][c] == MONSTER]

    while min_heap:
        dist, current = heapq.heappop(min_heap)  # Get the node with the minimum distance from the heap

        if current in food_positions:  # If we reached a food position, reconstruct the path
            path = []
            while current:
                path.append(current)
                current = parent[current[0]][current[1]]
            path = list(reversed(path))
            
            # Calculate the score based on path length and other criteria
            score = len(path) - 1  # Subtract 1 for the initial position

            # Update ghost paths
            for ghost_path in ghost_paths:
                ghost_path["path"].append(ghost_path["mat_pos"])
            
            return path, len(path), ghost_paths, score

        if dist > distance[current[0]][current[1]]:  # Skip if this node has already been processed with a shorter distance
            continue

        # Explore neighboring nodes
        for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            new_r, new_c = current[0] + dr, current[1] + dc

            if 0 <= new_r < rows and 0 <= new_c < cols and map[new_r][new_c] == EMPTY:  # Check if the neighbor is a valid path
                new_dist = dist + 1

                if new_dist < distance[new_r][new_c]:  # Update distance and parent if a shorter path is found
                    distance[new_r][new_c] = new_dist
                    parent[new_r][new_c] = current
                    heapq.heappush(min_heap, (new_dist, (new_r, new_c)))  # Add the neighbor to the priority queue

    # If no path to the food is found, return an empty path, empty ghost paths, and a score of 0
    return [], 0, [], 0
