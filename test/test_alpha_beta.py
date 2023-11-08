from app.settings import BASE_DIR
from app.utils.read_map import read_map
from app.search_algo import search_algo
from app.graphic import draw_pane, play_game
import time

MAP_DIR = BASE_DIR / "app" / "maps"
TEST_ALGO_NAME = "alpha_beta_search"


def gen_test_case():
    # Create test case 1 (.map1.txt - have solution)
    if not (MAP_DIR / ".map1.txt").exists():
        with open(MAP_DIR / ".map1.txt", "w") as f:
            f.write("10 20\n")
            f.write("1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1\n")
            f.write("1 0 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 1 \n")
            f.write("1 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 1 1\n")
            f.write("1 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 1\n")
            f.write("1 2 2 2 1 2 2 2 2 2 1 1 1 2 1 2 1 2 1 1\n")
            f.write("1 2 2 2 1 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2\n")
            f.write("1 2 2 1 1 2 1 2 1 2 2 2 2 2 1 2 1 2 1 1\n")
            f.write("1 2 2 2 1 2 2 2 3 2 2 1 2 2 2 2 2 2 2 1\n")
            f.write("1 2 2 3 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 1\n")
            f.write("1 2 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 2 1\n")
            f.write("1 1\n")
            f.close()

    # Create test case 2 (.map2.txt - no solution)
    if not (MAP_DIR / ".map2.txt").exists():
        with open(MAP_DIR / ".map2.txt", "w") as f:
            f.write("10 20\n")
            f.write("1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1\n")
            f.write("1 0 1 2 2 2 1 2 2 2 1 1 1 2 1 2 1 2 1 1 \n")
            f.write("1 2 2 1 1 2 2 2 1 2 1 1 1 2 1 2 2 2 1 1\n")
            f.write("1 1 2 1 1 2 2 2 1 2 2 2 2 2 1 2 1 2 2 1\n")
            f.write("1 2 2 2 1 2 2 2 3 2 1 1 1 2 1 2 1 2 1 1\n")
            f.write("1 1 2 1 1 2 2 2 1 2 1 3 1 2 1 2 1 2 1 1\n")
            f.write("1 2 2 1 1 2 1 2 1 2 2 2 2 2 1 2 1 2 1 1\n")
            f.write("1 1 2 2 2 2 1 2 1 2 1 3 2 2 1 2 1 2 1 1\n")
            f.write("1 2 2 1 1 2 1 2 2 2 1 2 2 2 2 2 2 2 1 1\n")
            f.write("1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1\n")
            f.write("1 1\n")
            f.close()


def undo_test_case():
    # delete all map test cases
    (MAP_DIR / ".map1.txt").unlink()
    (MAP_DIR / ".map2.txt").unlink()


def get_max_score(map):
    score = 0
    for row in map:
        for cell in row:
            if cell == 2:
                score += 1
    return score


def test_alpha_beta():
    pass
    # Generate test cases
    gen_test_case()

    # Check search algo run correctly in test case 1 (level 4)
    try:
        map, map_size, pacman_pos = read_map(".map1.txt")
    except Exception as e:
        print("Test failed")
    try:
        # Draw the initial state of the game
        pac_man_id, ghost_ids, food_ids, score_table_id = draw_pane(
            map, map_size, pacman_pos
        )
    except Exception as e:
        print("Test failed")
        print(e)

    try:
        pacman_path, ghosts_path = search_algo(
            TEST_ALGO_NAME, map, map_size, pacman_pos, 4
        )
    except Exception as e:
        print("Test failed")
        print(e)

    score = get_max_score(map)
    try:
        play_game(
            map_size,
            pac_man_id,
            ghost_ids,
            food_ids,
            score_table_id,
            pacman_path,
            ghosts_path,
            score,
            time_frame=0.3,
        )
    except Exception as e:
        print(e)
        pass

    # Undo test cases
    undo_test_case()
