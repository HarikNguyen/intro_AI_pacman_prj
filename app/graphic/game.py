""" 
Game (PacmanGraphic object) need the map, map_size, pacman_start_pos, to draw the initial 
state of the game.
And the returned results by search algorithm to draw the animation of the game like pacman_path,
pacman_score, ghost paths (ghosts_path if ghost move).
"""
from app.utils.graphic import *
from app.constants.graphic import *
def draw_pane(map, map_size, pacman_pos, grid_size=DEFAULT_GRID_SIZE, zoom=1.0, time_frame = 0.0):
    
    # Init background
    graphic_init()

    wait_for_close()