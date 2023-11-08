# Demonstrate the problem by score:
# - We set for each movement, score will be decreased by 1 (-1)
# - We set for each food eaten, score will be increased by 20 (+20)
# - We set for each ghost eaten, score will be decreased by 1000000 (-1000000) ~ - inf
# (negative infinity) for demonstrate this is the worst case for pacman
# depth (tree depth) = # of movement steps

from app.constants import (
    X,
    Y,
    UP,
    DOWN,
    LEFT,
    RIGHT,
    STOP,
    FOOD,
    MOVE_SCORE,
    MONSTER,
    WALL,
    ROAD,
)
from app.utils.algo_shared_func import (
    get_neighbors,
)
from app.utils.ghost import get_ghost_paths
from random import randint

DEPTH = 30
FAIL_SCORE = -1000000


def alpha_beta_search(map, map_size, pacman_pos):
    result_pacman_path = []
    result_ghosts_paths = []

    ghosts_pos = []
    for i in range(map_size[X]):
        for j in range(map_size[Y]):
            if map[i][j] == MONSTER:
                ghosts_pos.append((i, j))
    new_map = copy_map(map)
    new_pacman_pos = pacman_pos
    new_ghosts_pos = ghosts_pos
    # remove MONSTER sign in new_map
    for ghost_pos in ghosts_pos:
        new_map[ghost_pos[0]][ghost_pos[1]] = ROAD
    result_pacman_path.append(new_pacman_pos)
    result_ghosts_paths.append(new_ghosts_pos)

    while True:
        if terminal_test(new_map, map_size, (new_map, new_pacman_pos, new_ghosts_pos)):
            break
        # update map state
        # for pacman
        new_pacman_pos = search(new_map, map_size, new_pacman_pos, new_ghosts_pos)
        result_pacman_path.append(new_pacman_pos)
        # for ghosts
        new_ghosts_pos = get_ghost_paths(
            new_map, map_size, new_pacman_pos, new_ghosts_pos
        )
        result_ghosts_paths.append(new_ghosts_pos)
        # update map (if pacman eat food)
        if new_map[new_pacman_pos[0]][new_pacman_pos[1]] == FOOD:
            new_map[new_pacman_pos[0]][new_pacman_pos[1]] = 0

    # transform result_ghosts_paths to list of dict [{"mat_pos": (x, y), "path": [(x, y), ...]}, ...]
    result_ghosts_paths_list_of_dict = []
    for ghosts_pos_id, ghosts_pos in enumerate(result_ghosts_paths):
        if ghosts_pos_id == 0:
            for ghost_pos in ghosts_pos:
                result_ghosts_paths_list_of_dict.append(
                    {"mat_pos": ghost_pos, "path": [ghost_pos]}
                )
        else:
            for ghost_pos_id, ghost_pos in enumerate(ghosts_pos):
                result_ghosts_paths_list_of_dict[ghost_pos_id]["path"].append(ghost_pos)

    return result_pacman_path, result_ghosts_paths_list_of_dict


def search(map, map_size, pacman_pos, ghosts_pos, depth=DEPTH):
    alpha = float("-inf")
    beta = float("inf")

    def alpha_beta_helper(map, map_size, node, depth=DEPTH, is_pacman_run=True):
        nonlocal alpha, beta
        if depth == 0 or terminal_test(map, map_size, node):
            return get_utility(map, node)

        if is_pacman_run:
            best_utility = float("-inf")
            old_pacman_pos = node[1]
            cur_map = node[0]
            ghosts_pos = node[2]
            neighbors = get_next_pacman_positions(
                cur_map, map_size, ghosts_pos, old_pacman_pos
            )
            for neighbor in neighbors:
                # set-up new node
                new_pacman_pos = neighbor

                # update map (if pacman eat food)
                new_map = copy_map(cur_map)
                if new_map[new_pacman_pos[0]][new_pacman_pos[1]] == FOOD:
                    new_map[new_pacman_pos[0]][new_pacman_pos[1]] = ROAD
                new_node = (new_map, new_pacman_pos, ghosts_pos)

                # calculate utility of new node
                utility = alpha_beta_helper(map, map_size, new_node, depth - 1, False)

                # update best utility (maximize)
                best_utility = max(best_utility, utility)

                # update alpha (maximize)
                alpha = max(alpha, best_utility)

                # prune
                if alpha >= beta:
                    break
            return best_utility
        else:
            best_utility = float("inf")
            cur_map = node[0]
            old_ghosts_pos = node[2]
            pacman_pos = node[1]
            next_ghosts_poss = get_next_ghosts_positions(
                node[0], map_size, old_ghosts_pos
            )

            for next_ghosts_pos in next_ghosts_poss:
                # set-up new node
                ghosts_pos = next_ghosts_pos

                # retain old map
                new_map = copy_map(cur_map)
                new_node = (new_map, pacman_pos, ghosts_pos)

                # calculate utility of new node
                best_utility = alpha_beta_helper(
                    map, map_size, new_node, depth - 1, True
                )

                # update best utility (minimize)
                beta = min(beta, best_utility)

                # prune
                if alpha >= beta:
                    break
            return best_utility

    # Start the alpha-beta search.
    node = (map, pacman_pos, ghosts_pos)
    cur_map = copy_map(map)
    best_utility = alpha_beta_helper(cur_map, map_size, node, depth)
    best_move = STOP
    neighbors = get_next_pacman_positions(map, map_size, ghosts_pos, pacman_pos)
    for neighbor in neighbors:
        new_node = (map, neighbor, ghosts_pos)
        utility = alpha_beta_helper(cur_map, map_size, new_node, depth, False)
        if utility >= best_utility:
            best_move = neighbor
            break
    # if pacman can't move, return random move
    if best_move == STOP:
        if len(neighbors) != 0:
            ran_index = randint(0, len(neighbors) - 1)
            best_move = neighbors[ran_index]
        else:
            best_move = pacman_pos
    return best_move


def print_map(map):
    for row in map:
        print(row)


def copy_map(map):
    new_map = []
    for row in map:
        new_map.append(row.copy())
    return new_map


def terminal_test(map, map_size, node):
    """State is terminal if pacman eat all food or ghost catch pacman

    Args:
        node: (pacman_pos, ghosts_pos)
    """
    cur_map, pacman_pos, ghosts_pos = node
    if pacman_pos in ghosts_pos:
        return True

    if is_no_food(cur_map):
        return True

    return False


def is_no_food(map):
    for row in map:
        for cell in row:
            if cell == FOOD:
                return False
    return True


def get_utility(map, node):
    """
    We set the depth = DEPTH so the utility will be:
        - FAIL_SCORE if pacman is caught by ghost
        - (# of old food - # of current food)*20 - depth*MOVE_SCORE otherwise
    """
    cur_map, pacman_pos, ghosts_pos = node
    old_food_count = count_food(map)
    current_food_count = count_food(cur_map)

    if pacman_pos in ghosts_pos:
        return FAIL_SCORE
    return (old_food_count - current_food_count) * 20 - DEPTH * MOVE_SCORE


def count_food(map):
    count = 0
    for row in map:
        for cell in row:
            if cell == FOOD:
                count += 1
    return count


def get_next_ghosts_positions(map, map_size, ghosts_pos):
    new_ghosts_pos = []
    # get all neighbors of ghosts
    ghosts_neighbors = {}
    for ghost_pos in ghosts_pos:
        ghosts_neighbors[ghost_pos] = get_neighbors(map, map_size, ghost_pos)

    # get all possible next positions of ghosts
    possible_len = sum([len(ghosts_neighbors[ghost_pos]) for ghost_pos in ghosts_pos])

    for possible_id in range(possible_len):
        new_ghosts_pos.append([])
        for ghost_pos in ghosts_pos:
            ghost_poss_len = len(ghosts_neighbors[ghost_pos])
            if ghost_poss_len != 0:
                new_ghosts_pos[possible_id].append(
                    ghosts_neighbors[ghost_pos][
                        possible_id % len(ghosts_neighbors[ghost_pos])
                    ]
                )
            else:
                new_ghosts_pos[possible_id].append(ghost_pos)

    return new_ghosts_pos


def get_next_pacman_positions(map, map_size, ghosts_pos, pacman_pos):
    new_pacman_pos = []

    # get all neighbors of pacman
    pacman_neighbors = get_neighbors(map, map_size, pacman_pos)

    # get all possible next positions of pacman
    for pacman_neighbor in pacman_neighbors:
        if pacman_neighbor not in ghosts_pos:
            new_pacman_pos.append(pacman_neighbor)

    # prior for this neighbor having food
    prior_neighbors = []
    for neighbor in new_pacman_pos:
        if map[neighbor[0]][neighbor[1]] == FOOD:
            # append to top of list
            prior_neighbors.insert(0, neighbor)
        else:
            # append to bottom of list
            prior_neighbors.append(neighbor)

    return prior_neighbors
