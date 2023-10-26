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
    # Init info pane
    grid_size = zoom * grid_size
    font_size = 24
    text_color = PACMAN_COLOR
    width = (map_size[Y] + 2) * grid_size
    base = (map_size[X] + 1) * grid_size
    height = base + INFO_PANE_HEIGHT
    screen_size = (width, height)

    # Init background
    graphic_init(width, height, background_color=BACKGROUND_COLOR)

    # Draw walls
    draw_wall(map, map_size, grid_size)
    refresh()

    # Draw pacman
    pacman_id = draw_pacman(map, map_size, pacman_pos, grid_size)
    refresh()

    # Draw food
    food_ids = draw_food(map, map_size, grid_size)

    # Draw ghost
    ghost_ids = []

    bind_esc_to_quit()

    return pacman_id, ghost_ids, food_ids


def play_game(
    map_size,
    pacman_id,
    ghost_ids,
    food_ids,
    pacman_path,
    ghost_paths,
    extract_score,
    time_frame=0.0,
):
    # define cur_score = 0
    curr_score = 0

    # convert pacman_path to direction_routing
    pacman_routing = convert_path_to_direction_routing(pacman_path)

    # each time frame update step by step
    frame_no = 0  # frame id counted when play
    while True:
        # check if pacman stop
        if frame_no == len(pacman_routing):
            wait_for_close()

        # pacman move
        pacman_direction = pacman_routing[frame_no]
        pacman_mat_pos = (
            pacman_path[frame_no][Y],
            pacman_path[frame_no][X],
        )  # matrix (x, y) --> screen (y,x)
        move_pacman(pacman_id, map_size, pacman_mat_pos, pacman_direction)
        # pacman eat food
        if pacman_path[frame_no] in list(food["key"] for food in food_ids):
            food_ids = remove_food(food_ids, pacman_path[frame_no])
            curr_score += 1
        # ghost move
        # for ghost_id, ghost_path in zip(ghost_ids, ghost_paths):
        #     ghost_direction = convert_path_to_direction_routing(ghost_path)[frame_no]
        #     move_pacman(ghost_id, ghost_path[frame_no], ghost_direction)
        #     refresh()

        # update frame id
        frame_no += 1

        # wait for time_frame
        sleep(time_frame)


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

    direction_routing[-1] = STOP

    return direction_routing
