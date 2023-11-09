""" This module contains functions to draw and remove food from screen
"""

from app.utils.graphic import *
from app.constants.graphic import *
from app.constants import *


def draw_food(map, map_size, grid_size, zoom=1.0):
    """Draw food to screen"""

    # calculate grid_size by zoom
    grid_size = grid_size * zoom

    food_ids = []

    for row_id, row in enumerate(map):
        for col_id, cell in enumerate(row):
            if cell == FOOD:
                # draw food
                screen_pos = matrix_to_screen((col_id, row_id), map_size, grid_size)
                food = circle(
                    screen_pos,
                    FOOD_SIZE * grid_size,
                    outline_color=FOOD_COLOR,
                    fill_color=FOOD_COLOR,
                    width=1,
                )
                food_ids.append({"key": (row_id, col_id), "id": food})
    return food_ids


def remove_food(food_ids, food_remove_pos):
    """Remove food from screen"""

    # remove food_remove_id in food_ids
    food_ids_removed = []
    food_remove_id = None
    for food in food_ids:
        if food["key"] != food_remove_pos:
            food_ids_removed.append(food)
        else:
            food_remove_id = food["id"]

    # remove food from screen
    remove_from_screen(food_remove_id)

    return food_ids_removed
