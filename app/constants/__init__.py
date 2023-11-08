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
ALGO_NAME = ["bfs", "dfs", "ucs", "a_star"]

# SCORE
EAT_FOOD_SCORE = 20
MOVE_SCORE = 1
