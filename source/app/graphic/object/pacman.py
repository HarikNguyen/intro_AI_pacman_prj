"""This module contains functions to draw and move pacman from screen
"""

from app.utils.graphic import *
from app.constants.graphic import *
from app.constants import *


def draw_pacman(map, map_size, pacman_start_pos, grid_size=DEFAULT_GRID_SIZE, zoom=1.0):
    row_id, col_id = pacman_start_pos
    screen_pos = matrix_to_screen((col_id, row_id), map_size, grid_size, zoom)
    endpoints = get_endpoints()

    width = PACMAN_OUTLINE_WIDTH
    outline_color = PACMAN_COLOR
    fill_color = PACMAN_COLOR

    return circle(
        screen_pos,
        PACMAN_SCALE * grid_size * zoom,
        outline_color=outline_color,
        fill_color=fill_color,
        endpoints=endpoints,
        width=width,
    )


def get_endpoints(direction=STOP, degree=120):
    delta = degree / 2

    if direction == LEFT:
        return (180 + delta, 180 - delta)
    elif direction == UP:
        return (90 + delta, 90 - delta)
    elif direction == RIGHT:
        return (0 + delta, 0 - delta)
    elif direction == DOWN:
        return (270 + delta, 270 - delta)
    else:
        return (0, 359)


def move_pacman(
    pacman_id, map_size, pacman_pos, direction, grid_size=DEFAULT_GRID_SIZE, zoom=1.0
):
    row_id, col_id = pacman_pos
    cur_pacman_pos = (col_id, row_id)  # matrix (x,y) --> screen (y, x)
    max_degree = 110

    screen_pos = matrix_to_screen(cur_pacman_pos, map_size, grid_size, zoom)
    if direction != STOP:
        endpoints = get_endpoints(direction, max_degree)
    else:
        endpoints = get_endpoints()
    move_circle(pacman_id, screen_pos, PACMAN_SCALE * grid_size * zoom, endpoints)
