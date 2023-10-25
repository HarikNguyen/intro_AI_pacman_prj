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

    wait_for_close()
