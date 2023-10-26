
from app.utils.graphic import *
from app.constants.graphic import *
from app.constants import *


def draw_food(map, map_size, grid_size):

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
                    width=1
                )
                food_ids.append({
                    "key": 1,
                    "id": food
                })
    return food_ids

def remove_food(food_ids, food_remove_id):
    # remove food_remove_id in food_ids
    food_ids_removed = []
    for food in food_ids:
        if food.id != food_remove_id:
            food_ids_removed.append(food)
    
    # remove food from screen
    remove_from_screen(food_remove_id)

    return food_ids_removed