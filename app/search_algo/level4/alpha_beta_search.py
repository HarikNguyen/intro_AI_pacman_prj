# Demonstrate the problem by score:
# - We set for each movement, score will be decreased by 1 (-1)
# - We set for each food eaten, score will be increased by 20 (+20)
# - We set for each ghost eaten, score will be decreased by 1000000 (-1000000) ~ - inf
# (negative infinity) for demonstrate this is the worst case for pacman
# depth (tree depth) = # of movement steps

from app.constants import (
    UP,
    DOWN,
    LEFT,
    RIGHT,
    STOP,
    FOOD,
)
from app.utils.algo_shared_func import (
    get_neighbors,
)

DEPTH = 3


def alpha_beta_search(map, map_size, pacman_pos):
    pass


def search(map, map_size, pacman_pos, ghosts_pos, depth=DEPTH):
    alpha = float("-inf")
    beta = float("inf")

    def alpha_beta_helper(map, map_size, node, depth=DEPTH, is_pacman_run=True):
        if depth == 0 or terminal_test(map, map_size, node):
            return get_utility(map, node)

        if is_pacman_run:
            best_utility = float("-inf")
            neighbors = get_neighbors(map, map_size, node[0])
            for neighbor in neighbors:
                utility = alpha_beta_helper(
                    map, map_size, (neighbor, node[1]), depth - 1, False
                )
                best_utility = max(best_utility, utility)
                alpha = max(alpha, best_utility)
                if alpha >= beta:
                    break
            return best_utility
        else:
            best_utility = float("inf")
            next_ghosts_poss = get_next_ghosts_positions(map, map_size, node[1])
            for next_ghosts_pos in next_ghosts_poss:
                best_utility = alpha_beta_helper(
                    map, map_size, (node[0], next_ghosts_pos), depth - 1, True
                )
                beta = min(beta, best_utility)
                if alpha >= beta:
                    break
            return best_utility

    # Start the alpha-beta search.

    best_utility = alpha_beta_helper(map, map_size, (pacman_pos, ghosts_pos), depth)
    best_move = STOP
    neighbors = get_neighbors(map, map_size, pacman_pos)
    for neighbor in neighbors:
        utility = alpha_beta_helper(map, map_size, (neighbor, ghosts_pos), depth, False)
        if utility == best_utility:
            best_move = neighbor
            break
    return best_move


def terminal_test(map, map_size, node):
    """State is terminal if pacman eat all food or ghost catch pacman

    Args:
        node: (pacman_pos, ghosts_pos)
    """
    pacman_pos, ghosts_pos = node
    if pacman_pos in ghosts_pos:
        return True

    if is_no_food(map):
        return True

    return False


def is_no_food(map):
    for row in map:
        for cell in row:
            if cell == FOOD:
                return False
    return True


def get_utility(map, node_pos):
    """
    Get the utility for pacman in map state
    If pacman
    """
    pass


def get_next_ghosts_positions(map, map_size, ghosts_pos):
    pass
