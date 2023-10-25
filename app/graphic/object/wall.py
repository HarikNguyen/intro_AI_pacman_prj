from app.utils.graphic import *
from app.constants.graphic import *
from app.constants import *


def draw_wall(map, map_size, grid_size=DEFAULT_GRID_SIZE):
    """
    Draw walls
    """
    for y_id, row_block in enumerate(map):
        for x_id, cell in enumerate(row_block):
            if cell == WALL:  # cell is wall
                # calculate the screen position
                screen_pos = matrix_to_screen((x_id, y_id), map_size, grid_size)
                # draw each quadrant of the square based on adjacent walls
                is_w_wall = is_wall(map, y_id, x_id - 1)
                is_e_wall = is_wall(map, y_id, x_id + 1)
                is_n_wall = is_wall(map, y_id - 1, x_id)
                is_s_wall = is_wall(map, y_id + 1, x_id)
                is_nw_wall = is_wall(map, y_id - 1, x_id - 1)
                is_sw_wall = is_wall(map, y_id + 1, x_id - 1)
                is_ne_wall = is_wall(map, y_id - 1, x_id + 1)
                is_se_wall = is_wall(map, y_id + 1, x_id + 1)

                # NE quadrant
                if (not is_n_wall) and (not is_e_wall):
                    # inner circle
                    circle(
                        screen_pos,
                        WALL_RADIUS * grid_size,
                        WALL_COLOR,
                        WALL_COLOR,
                        (0, 91),
                        "arc",
                    )
                if (is_n_wall) and (not is_e_wall):
                    # vertical line
                    line(
                        add_2_point(screen_pos, (grid_size * WALL_RADIUS, 0)),
                        add_2_point(
                            screen_pos,
                            (grid_size * WALL_RADIUS, grid_size * (-0.5) - 1),
                        ),
                        WALL_COLOR,
                    )
                if (not is_n_wall) and (is_e_wall):
                    # horizontal line
                    line(
                        add_2_point(screen_pos, (0, grid_size * (-1) * WALL_RADIUS)),
                        add_2_point(
                            screen_pos,
                            (grid_size * 0.5 + 1, grid_size * (-1) * WALL_RADIUS),
                        ),
                        WALL_COLOR,
                    )
                if (is_n_wall) and (is_e_wall) and (not is_ne_wall):
                    # outer circle
                    circle(
                        add_2_point(
                            screen_pos,
                            (
                                grid_size * 2 * WALL_RADIUS,
                                grid_size * (-2) * WALL_RADIUS,
                            ),
                        ),
                        WALL_RADIUS * grid_size - 1,
                        WALL_COLOR,
                        WALL_COLOR,
                        (180, 271),
                        "arc",
                    )
                    line(
                        add_2_point(
                            screen_pos,
                            (
                                grid_size * 2 * WALL_RADIUS - 1,
                                grid_size * (-1) * WALL_RADIUS,
                            ),
                        ),
                        add_2_point(
                            screen_pos,
                            (grid_size * 0.5 + 1, grid_size * (-1) * WALL_RADIUS),
                        ),
                        WALL_COLOR,
                    )
                    line(
                        add_2_point(
                            screen_pos,
                            (
                                grid_size * WALL_RADIUS,
                                grid_size * (-2) * WALL_RADIUS + 1,
                            ),
                        ),
                        add_2_point(
                            screen_pos, (grid_size * WALL_RADIUS, grid_size * (-0.5))
                        ),
                        WALL_COLOR,
                    )

                # NW quadrant
                if (not is_n_wall) and (not is_w_wall):
                    # inner circle
                    circle(
                        screen_pos,
                        WALL_RADIUS * grid_size,
                        WALL_COLOR,
                        WALL_COLOR,
                        (90, 181),
                        "arc",
                    )
                if (is_n_wall) and (not is_w_wall):
                    # vertical line
                    line(
                        add_2_point(screen_pos, (grid_size * (-1) * WALL_RADIUS, 0)),
                        add_2_point(
                            screen_pos,
                            (grid_size * (-1) * WALL_RADIUS, grid_size * (-0.5) - 1),
                        ),
                        WALL_COLOR,
                    )
                if (not is_n_wall) and (is_w_wall):
                    # horizontal line
                    line(
                        add_2_point(screen_pos, (0, grid_size * (-1) * WALL_RADIUS)),
                        add_2_point(
                            screen_pos,
                            (grid_size * (-0.5) - 1, grid_size * (-1) * WALL_RADIUS),
                        ),
                        WALL_COLOR,
                    )
                if (is_n_wall) and (is_w_wall) and (not is_nw_wall):
                    # outer circle
                    circle(
                        add_2_point(
                            screen_pos,
                            (
                                grid_size * (-2) * WALL_RADIUS,
                                grid_size * (-2) * WALL_RADIUS,
                            ),
                        ),
                        WALL_RADIUS * grid_size - 1,
                        WALL_COLOR,
                        WALL_COLOR,
                        (270, 361),
                        "arc",
                    )
                    line(
                        add_2_point(
                            screen_pos,
                            (
                                grid_size * (-2) * WALL_RADIUS + 1,
                                grid_size * (-1) * WALL_RADIUS,
                            ),
                        ),
                        add_2_point(
                            screen_pos,
                            (grid_size * (-0.5), grid_size * (-1) * WALL_RADIUS),
                        ),
                        WALL_COLOR,
                    )
                    line(
                        add_2_point(
                            screen_pos,
                            (
                                grid_size * (-1) * WALL_RADIUS,
                                grid_size * (-2) * WALL_RADIUS + 1,
                            ),
                        ),
                        add_2_point(
                            screen_pos,
                            (grid_size * (-1) * WALL_RADIUS, grid_size * (-0.5)),
                        ),
                        WALL_COLOR,
                    )

                # SE quadrant
                if (not is_s_wall) and (not is_e_wall):
                    # inner circle
                    circle(
                        screen_pos,
                        WALL_RADIUS * grid_size,
                        WALL_COLOR,
                        WALL_COLOR,
                        (270, 361),
                        "arc",
                    )
                if (is_s_wall) and (not is_e_wall):
                    # vertical line
                    line(
                        add_2_point(screen_pos, (grid_size * WALL_RADIUS, 0)),
                        add_2_point(
                            screen_pos, (grid_size * WALL_RADIUS, grid_size * (0.5) + 1)
                        ),
                        WALL_COLOR,
                    )
                if (not is_s_wall) and (is_e_wall):
                    # horizontal line
                    line(
                        add_2_point(screen_pos, (0, grid_size * (1) * WALL_RADIUS)),
                        add_2_point(
                            screen_pos,
                            (grid_size * 0.5 + 1, grid_size * (1) * WALL_RADIUS),
                        ),
                        WALL_COLOR,
                    )
                if (is_s_wall) and (is_e_wall) and (not is_se_wall):
                    # outer circle
                    circle(
                        add_2_point(
                            screen_pos,
                            (
                                grid_size * 2 * WALL_RADIUS,
                                grid_size * (2) * WALL_RADIUS,
                            ),
                        ),
                        WALL_RADIUS * grid_size - 1,
                        WALL_COLOR,
                        WALL_COLOR,
                        (90, 181),
                        "arc",
                    )
                    line(
                        add_2_point(
                            screen_pos,
                            (
                                grid_size * 2 * WALL_RADIUS - 1,
                                grid_size * (1) * WALL_RADIUS,
                            ),
                        ),
                        add_2_point(
                            screen_pos, (grid_size * 0.5, grid_size * (1) * WALL_RADIUS)
                        ),
                        WALL_COLOR,
                    )
                    line(
                        add_2_point(
                            screen_pos,
                            (
                                grid_size * WALL_RADIUS,
                                grid_size * (2) * WALL_RADIUS - 1,
                            ),
                        ),
                        add_2_point(
                            screen_pos, (grid_size * WALL_RADIUS, grid_size * (0.5))
                        ),
                        WALL_COLOR,
                    )

                # SW quadrant
                if (not is_s_wall) and (not is_w_wall):
                    # inner circle
                    circle(
                        screen_pos,
                        WALL_RADIUS * grid_size,
                        WALL_COLOR,
                        WALL_COLOR,
                        (180, 271),
                        "arc",
                    )
                if (is_s_wall) and (not is_w_wall):
                    # vertical line
                    line(
                        add_2_point(screen_pos, (grid_size * (-1) * WALL_RADIUS, 0)),
                        add_2_point(
                            screen_pos,
                            (grid_size * (-1) * WALL_RADIUS, grid_size * (0.5) + 1),
                        ),
                        WALL_COLOR,
                    )
                if (not is_s_wall) and (is_w_wall):
                    # horizontal line
                    line(
                        add_2_point(screen_pos, (0, grid_size * (1) * WALL_RADIUS)),
                        add_2_point(
                            screen_pos,
                            (grid_size * (-0.5) - 1, grid_size * (1) * WALL_RADIUS),
                        ),
                        WALL_COLOR,
                    )
                if (is_s_wall) and (is_w_wall) and (not is_sw_wall):
                    # outer circle
                    circle(
                        add_2_point(
                            screen_pos,
                            (
                                grid_size * (-2) * WALL_RADIUS,
                                grid_size * (2) * WALL_RADIUS,
                            ),
                        ),
                        WALL_RADIUS * grid_size - 1,
                        WALL_COLOR,
                        WALL_COLOR,
                        (0, 91),
                        "arc",
                    )
                    line(
                        add_2_point(
                            screen_pos,
                            (
                                grid_size * (-2) * WALL_RADIUS + 1,
                                grid_size * (1) * WALL_RADIUS,
                            ),
                        ),
                        add_2_point(
                            screen_pos,
                            (grid_size * (-0.5), grid_size * (1) * WALL_RADIUS),
                        ),
                        WALL_COLOR,
                    )
                    line(
                        add_2_point(
                            screen_pos,
                            (
                                grid_size * (-1) * WALL_RADIUS,
                                grid_size * (2) * WALL_RADIUS - 1,
                            ),
                        ),
                        add_2_point(
                            screen_pos,
                            (grid_size * (-1) * WALL_RADIUS, grid_size * (0.5)),
                        ),
                        WALL_COLOR,
                    )


def is_wall(map, y, x):
    if x < 0 or y < 0:
        return False
    if y >= len(map) or x >= len(map[0]):
        return False
    return map[y][x] == WALL
