from app.constants import MONSTER


def init_ghost_paths(map):
    # Define ghost_paths list of dict
    ghost_paths = []
    for row_id, row in enumerate(map):
        for col_id, cell in enumerate(row):
            if cell == MONSTER:
                ghost_paths.append({"mat_pos": (row_id, col_id), "path": []})

    return ghost_paths
