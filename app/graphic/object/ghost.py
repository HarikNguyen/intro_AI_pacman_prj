"""This module contains functions to draw and move ghost from screen
"""

import random
from app.utils.graphic import *
from app.constants.graphic import *
from app.constants import *

ghost_colors = []


def draw_ghost(ghost_mat_pos, map_size, grid_size=DEFAULT_GRID_SIZE):
    global ghost_colors
    screen_pos_x, screen_pos_y = matrix_to_screen(ghost_mat_pos, map_size, grid_size)

    # Draw ghost body
    ghost_body_coords = []
    for x, y in GHOST_SHAPE:
        ghost_body_coords.append(
            (
                x * grid_size * GHOST_SIZE + screen_pos_x,
                y * grid_size * GHOST_SIZE + screen_pos_y,
            )
        )

    # random ghost color (r,g,b) != PACMAN_COLOR != FOOD_COLOR != WALL_COLOR
    invalid_colors = [PACMAN_COLOR, FOOD_COLOR, WALL_COLOR]
    for color in ghost_colors:
        invalid_colors.append(color)

    while True:
        ghost_color = format_color(
            random.random(),  # r [0,1]
            random.random(),  # g [0,1]
            random.random(),  # b [0,1]
        )
        if ghost_color not in invalid_colors:
            break

    ghost_colors.append(ghost_color)

    ghost_body_id = polygon(ghost_body_coords, ghost_color, filled=True)

    # Draw ghost eyes and pupils
    dx = 0
    dy = 0

    left_eye_id = circle(
        (
            screen_pos_x + grid_size * GHOST_SIZE * (-0.3 + dx / 1.5),
            screen_pos_y - grid_size * GHOST_SIZE * (0.3 - dy / 1.5),
        ),
        grid_size * GHOST_SIZE * 0.2,
        WHITE,
        WHITE,
    )
    right_eye_id = circle(
        (
            screen_pos_x + grid_size * GHOST_SIZE * (0.3 + dx / 1.5),
            screen_pos_y - grid_size * GHOST_SIZE * (0.3 - dy / 1.5),
        ),
        grid_size * GHOST_SIZE * 0.2,
        WHITE,
        WHITE,
    )
    ghost_left_pupil_id = circle(
        (
            screen_pos_x + grid_size * GHOST_SIZE * (-0.3 + dx),
            screen_pos_y - grid_size * GHOST_SIZE * (0.3 - dy),
        ),
        grid_size * GHOST_SIZE * 0.08,
        BLACK,
        BLACK,
    )
    ghost_right_pupil_id = circle(
        (
            screen_pos_x + grid_size * GHOST_SIZE * (0.3 + dx),
            screen_pos_y - grid_size * GHOST_SIZE * (0.3 - dy),
        ),
        grid_size * GHOST_SIZE * 0.08,
        BLACK,
        BLACK,
    )

    ghost_id_list = [
        ghost_body_id,
        left_eye_id,
        right_eye_id,
        ghost_left_pupil_id,
        ghost_right_pupil_id,
    ]

    return ghost_id_list


def draw_all_ghost(map, map_size, grid_size=DEFAULT_GRID_SIZE):
    ghost_ids = []
    for row_id, row in enumerate(map):
        for col_id, cell in enumerate(row):
            if cell == MONSTER:
                ghost_mat_pos = (col_id, row_id)
                ghost_id_list = draw_ghost(ghost_mat_pos, map_size, grid_size)
                ghost_id_dict = {"key": (row_id, col_id), "id": ghost_id_list}
                ghost_ids.append(ghost_id_dict)

    return ghost_ids


def move_ghost(
    ghost_parts_id, ghost_mat_position, direction, map_size, grid_size=DEFAULT_GRID_SIZE
):
    # move eyes by direction
    move_eyes(ghost_parts_id[1:], ghost_mat_position, direction, map_size, grid_size)
    refresh()

    # move body by direction
    ghost_body_step = get_ghost_step(direction, grid_size)
    for ghost_part_id in ghost_parts_id:
        move_by(ghost_part_id, ghost_body_step)
    refresh()

    # move eyes by direction (stop)
    move_eyes(ghost_parts_id[1:], ghost_mat_position, STOP, map_size, grid_size)
    refresh()


def move_eyes(
    eye_id, ghost_mat_position, direction, map_size, grid_size=DEFAULT_GRID_SIZE
):
    screen_pos_x, screen_pos_y = matrix_to_screen(
        (ghost_mat_position[Y], ghost_mat_position[X]), map_size, grid_size
    )

    dx = 0
    dy = 0

    if direction == UP:
        dy -= 0.2
    elif direction == DOWN:
        dy += 0.2
    elif direction == LEFT:
        dx -= 0.2
    elif direction == RIGHT:
        dx += 0.2
    else:
        dx = 0
        dy = 0

    left_eye_id = eye_id[0]
    right_eye_id = eye_id[1]
    left_pupil_id = eye_id[2]
    right_pupil_id = eye_id[3]

    move_circle(
        left_eye_id,
        (
            screen_pos_x + grid_size * GHOST_SIZE * (-0.3 + dx / 1.5),
            screen_pos_y - grid_size * GHOST_SIZE * (0.3 - dy / 1.5),
        ),
        grid_size * GHOST_SIZE * 0.2,
    )
    move_circle(
        right_eye_id,
        (
            screen_pos_x + grid_size * GHOST_SIZE * (0.3 + dx / 1.5),
            screen_pos_y - grid_size * GHOST_SIZE * (0.3 - dy / 1.5),
        ),
        grid_size * GHOST_SIZE * 0.2,
    )
    move_circle(
        left_pupil_id,
        (
            screen_pos_x + grid_size * GHOST_SIZE * (-0.3 + dx),
            screen_pos_y - grid_size * GHOST_SIZE * (0.3 - dy),
        ),
        grid_size * GHOST_SIZE * 0.08,
    )
    move_circle(
        right_pupil_id,
        (
            screen_pos_x + grid_size * GHOST_SIZE * (0.3 + dx),
            screen_pos_y - grid_size * GHOST_SIZE * (0.3 - dy),
        ),
        grid_size * GHOST_SIZE * 0.08,
    )


def get_ghost_step(direction, grid_size=DEFAULT_GRID_SIZE):
    if direction == UP:
        return (0, -MOVE_STEP * grid_size)
    elif direction == DOWN:
        return (0, MOVE_STEP * grid_size)
    elif direction == LEFT:
        return (-MOVE_STEP * grid_size, 0)
    elif direction == RIGHT:
        return (MOVE_STEP * grid_size, 0)
    else:
        return (0, 0)
