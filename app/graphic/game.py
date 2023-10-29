""" 
Game (PacmanGraphic object) need the map, map_size, pacman_start_pos, to draw the initial 
state of the game.
And the returned results by search algorithm to draw the animation of the game like pacman_path,
pacman_score, ghost paths (ghosts_path if ghost move).
"""
from app.utils.graphic import *
from app.constants.graphic import *
from app.constants import *
from .object import *


def draw_pane(
    map, map_size, pacman_pos, grid_size=DEFAULT_GRID_SIZE, zoom=1.0, time_frame=0.0
):
    """Draw pacman pane to window (wall, pacman, ghosts, foods)

    Args:
        map (list of list): map (matrix)
        map_size (tuple of int): (map_col, map_row)
        pacman_pos (tuple of int): (row_id, col_id)
        grid_size (float, optional): grid size on screen. Defaults to DEFAULT_GRID_SIZE.
        zoom (float, optional): zoom map (RECOMMEND DON'T CHANGE). Defaults to 1.0.
        time_frame (float, optional): Time per frame. Defaults to 0.0.

    Returns:
        pacman_id (int): pacman_canvas_object id
        ghost_ids (list): list of {key: (ghost's position in matrix), id: ghost canvas object id}
        food_ids (list): list of {key: (food's position in matrix), id: food canvas object id}

    """
    # Init info pane
    grid_size = grid_size
    font_size = 24
    text_color = PACMAN_COLOR
    width = (map_size[Y] + 1) * grid_size * zoom
    base = (map_size[X] + 1) * grid_size * zoom
    height = base + INFO_PANE_HEIGHT
    screen_size = (width, height)

    # Init background
    graphic_init(width, height, background_color=BACKGROUND_COLOR)

    # Draw walls
    draw_wall(map, map_size, grid_size, zoom)
    refresh()

    # Draw pacman
    pacman_id = draw_pacman(map, map_size, pacman_pos, grid_size, zoom)
    refresh()

    # Draw food
    food_ids = draw_food(map, map_size, grid_size, zoom)

    # Draw ghost
    ghost_ids = draw_all_ghost(map, map_size, grid_size, zoom)

    # Draw score table
    score_table_id = draw_score_table_text(map_size, grid_size, zoom)

    bind_esc_to_quit()

    return pacman_id, ghost_ids, food_ids, score_table_id


def play_game(
    map_size,
    pacman_id,
    ghost_ids,
    food_ids,
    score_table_id,
    pacman_path,
    ghost_paths,
    extract_score,
    grid_size=DEFAULT_GRID_SIZE,
    zoom=1.0,
    time_frame=0.0,
):
    """play or implement all action of pacman, food, score and ghosts based on the returned results by search algorithm

    Args:
        map_size (tuple of int): (map_col, map_row)
        pacman_id (int): pacman_canvas_object id
        ghost_ids (list): list of {key: (ghost's position in matrix), id: ghost canvas object id}
        food_ids (list): list of {key: (food's position in matrix), id: food canvas object id}
        pacman_path (list of tuple): pacman_path
        ghost_paths (list of dict): ghost_paths list({"mat_pos": (row_id, col_id), "path": ghost_paths(list of tuple)})
        extract_score (function): extract score from pacman_path
        time_frame (float, optional): Time per frame. Defaults to 0.0.
    """
    # define variable
    is_win = False
    is_fail = False
    is_eat = False
    # define cur_score = 0
    curr_score = 0
    # convert pacman_path to direction_routing
    pacman_routing = convert_path_to_direction_routing(pacman_path)
    # convert ghost_paths to direction_routing
    ghost_routing = []
    for ghost_id in ghost_ids:
        ghost_routing_list = None
        ghost_path = []
        if (
            len(get_ghost_path(ghost_paths, ghost_id["key"])) == 0
            or get_ghost_path(ghost_paths, ghost_id["key"]) == STOP
        ):
            ghost_routing_list = [STOP] * len(pacman_routing)
            ghost_path = [ghost_id["key"]] * len(pacman_routing)
        else:
            ghost_routing_list = convert_path_to_direction_routing(
                get_ghost_path(ghost_paths, ghost_id["key"])
            )
            ghost_path = get_ghost_path(ghost_paths, ghost_id["key"])
        ghost_routing.append(
            {
                "key": ghost_id["key"],
                "ghost_id_list": ghost_id["id"],
                "ghost_routing": ghost_routing_list,
                "ghost_path": ghost_path,
            }
        )

    # each time frame update step by step
    frame_no = 0  # frame id counted when play
    while True:
        # pacman move
        pacman_direction = pacman_routing[frame_no]
        pacman_mat_pos = (
            pacman_path[frame_no][Y],
            pacman_path[frame_no][X],
        )  # matrix (x, y) --> screen (y,x)
        move_pacman(
            pacman_id, map_size, pacman_mat_pos, pacman_direction, grid_size, zoom
        )

        # pacman eat food
        if pacman_path[frame_no] in list(food["key"] for food in food_ids):
            food_ids = remove_food(food_ids, pacman_path[frame_no])
            curr_score = update_current_score(curr_score, True)
            is_eat = True
        else:
            # update state when pacman move
            curr_score = update_current_score(curr_score)
            is_eat = False


        # ghost move
        for ghost_ in ghost_routing:
            ghost_mat_pos = ghost_["ghost_path"][frame_no]
            ghost_id_list = ghost_["ghost_id_list"]
            ghost_direction = ghost_["ghost_routing"][frame_no]
            move_ghost(
                ghost_id_list, ghost_mat_pos, ghost_direction, map_size, grid_size, zoom
            )
            # check if pacman and ghost meet
            if (
                pacman_path[frame_no][X] == ghost_mat_pos[X]
                and pacman_path[frame_no][Y] == ghost_mat_pos[Y]
            ):
                is_fail = True
            

        # update frame id
        frame_no += 1

        # check if pacman win
        if len(food_ids) == 0 or curr_score == extract_score:
            is_win = True

        # update score table
        update_score(score_table_id, curr_score, is_fail, is_win, is_eat)

        # check if pacman stop
        if frame_no == len(pacman_routing):
            break

        # wait for time_frame
        sleep(time_frame)

    # wait for close
    wait_for_close()


def convert_path_to_direction_routing(path):
    direction_routing = [STOP]
    for path_id, cur_pos in enumerate(path[:-1]):
        next_pos = path[path_id + 1]

        # check to Left
        if next_pos[Y] - cur_pos[Y] < 0:
            direction_routing.append(LEFT)
        # check to Right
        elif next_pos[Y] - cur_pos[Y] > 0:
            direction_routing.append(RIGHT)
        # check to Up
        elif next_pos[X] - cur_pos[X] < 0:
            direction_routing.append(UP)
        # check to Down
        elif next_pos[X] - cur_pos[X] > 0:
            direction_routing.append(DOWN)
        else:
            pass

    return direction_routing


def get_ghost_path(ghost_paths, ghost_mat_pos):
    for ghost_path in ghost_paths:
        if ghost_path["mat_pos"] == ghost_mat_pos:
            return ghost_path["path"]
    return STOP


def update_current_score(curr_score, is_eat_food=False):
    if is_eat_food:
        curr_score += EAT_FOOD_SCORE
    else:
        curr_score += MOVE_SCORE
    return curr_score