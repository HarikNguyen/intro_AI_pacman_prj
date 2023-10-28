from app.constants.graphic import *
from app.constants import *
from app.utils.graphic import *

def draw_score_table_text(map_size, grid_size=DEFAULT_GRID_SIZE, zoom=1.0):

    # add text with content score: 0
    text_mat_pos = (2, map_size[X])
    text_screen_pos = matrix_to_screen(text_mat_pos, map_size, grid_size, zoom)

    score_table_id = text(text_screen_pos, SCORE_COLOR, "SCORE: 0")

    return score_table_id

def update_score(score_table_id, score, is_fail=False, is_win=False):
    # update score color
    if is_fail:
        change_color(score_table_id, FAIL_COLOR)
        change_text(score_table_id, "FAIL")
    elif is_win:
        change_color(score_table_id, WIN_COLOR)
        # update score text
        change_text(score_table_id, "SCORE: " + str(score))
    else:
        pass
    
    