from app.constants import WALL, FOOD, MONSTER, X, Y, ROAD

def is_food(map, pos):
    return map[pos[X]][pos[Y]] == FOOD


def is_wall(map, pos):
    return map[pos[X]][pos[Y]] == WALL


def is_monster(map, pos):
    return map[pos[X]][pos[Y]] == MONSTER


def is_road_for_ghost(map, pos):
    return (
        map[pos[X]][pos[Y]] == ROAD
        or map[pos[X]][pos[Y]] == FOOD
        or map[pos[X]][pos[Y]] == MONSTER
    )


def is_in_map(map_size, pos):
    return 0 <= pos[X] < map_size[X] and 0 <= pos[Y] < map_size[Y]


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
            neighbors.append((neighbor_x, neighbor_y))

    return neighbors
