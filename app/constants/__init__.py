""" Constants for the search algorithm
"""

ROAD = 0
WALL = 1
FOOD = 2
MONSTER = 3
INVISIBILITY = 4

# X(0) and Y(1) are the alias for indexes of position tuple
X = 0
Y = 1

# Define Algo_name list
ALGO_NAME = ["bfs", "dfs", "ucs", "a_star", "alpha_beta_search"]

# SCORE
EAT_FOOD_SCORE = 20
MOVE_SCORE = 1

# Define direction
UP = "up"
DOWN = "down"
LEFT = "left"
RIGHT = "right"
STOP = None  # Don't move

# Define direction vector
DIRECTION_VECTOR = {
    UP: (-1, 0),
    DOWN: (1, 0),
    LEFT: (0, -1),
    RIGHT: (0, 1),
}
