"""This module contains all the constants related to the graphic of the game.
"""
from app.utils.graphic import format_color, color_to_vector

#######################################################################################################################
########################################### GRAPHIC CONSTANTS #########################################################

DEFAULT_GRID_SIZE = 30.0
INFO_PANE_HEIGHT = 35
BACKGROUND_COLOR = format_color(42 / 255, 42 / 255, 45 / 255)
WALL_COLOR = format_color(0.0 / 255.0, 51.0 / 255.0, 255.0 / 255.0)
INFO_PANE_COLOR = format_color(0.4, 0.4, 0)
SCORE_COLOR = format_color(0.9, 0.9, 0.9)
MOVE_STEP = 1

WHITE = format_color(1.0, 1.0, 1.0)
BLACK = format_color(0.0, 0.0, 0.0)

#######################################################################################################################
########################################### PACMAN GRAPHIC ############################################################

PACMAN_OUTLINE_WIDTH = 2
PACMAN_CAPTURE_OUTLINE_WIDTH = 4
PACMAN_COLOR = format_color(255.0 / 255.0, 255.0 / 255.0, 61.0 / 255)
PACMAN_SCALE = 0.5
# pacman_speed = 0.25

#######################################################################################################################
########################################### GHOST GRAPHIC #############################################################
GHOST_COLORS = []
GHOST_COLORS.append(format_color(0.9, 0, 0))  # Red
GHOST_COLORS.append(format_color(0, 0.3, 0.9))  # Blue
GHOST_COLORS.append(format_color(0.98, 0.41, 0.07))  # Orange
GHOST_COLORS.append(format_color(0.1, 0.75, 0.7))  # Green
GHOST_COLORS.append(format_color(1.0, 0.6, 0.0))  # Yellow
GHOST_COLORS.append(format_color(0.4, 0.13, 0.91))  # Purple

GHOST_SHAPE = [
    (0, 0.3),
    (0.25, 0.75),
    (0.5, 0.3),
    (0.75, 0.75),
    (0.75, -0.5),
    (0.5, -0.75),
    (-0.5, -0.75),
    (-0.75, -0.5),
    (-0.75, 0.75),
    (-0.5, 0.3),
    (-0.25, 0.75),
]
GHOST_SIZE = 0.65
SCARED_COLOR = format_color(1, 1, 1)

GHOST_VEC_COLORS = map(color_to_vector, GHOST_COLORS)


#######################################################################################################################
########################################### FOOD GRAPHIC ##############################################################
FOOD_COLOR = format_color(245, 208, 240)
FOOD_SIZE = 0.14

#######################################################################################################################
########################################### WALL GRAPHIC ##############################################################
WALL_RADIUS = 0.15

#######################################################################################################################
########################################### DIRECTION #################################################################
UP = "up"
DOWN = "down"
LEFT = "left"
RIGHT = "right"
STOP = None  # Don't move
