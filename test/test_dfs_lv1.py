from app.settings import BASE_DIR
from app.utils.read_map import read_map
from app.search_algo import search_algo
from app.graphic import draw_pane, play_game

MAP_DIR = BASE_DIR / "app" / "maps"
TEST_ALGO_NAME = "dfs"


def gen_test_case():
    # Create test case 1 (.map1.txt - have solution)
    if not (MAP_DIR / ".map1.txt").exists():
        with open(MAP_DIR / ".map1.txt", "w") as f:
            f.write("8 8\n")
            f.write("1 1 1 1 1 1 1 1\n")
            f.write("1 0 0 0 0 1 0 1\n")
            f.write("1 1 1 0 0 0 0 1\n")
            f.write("1 0 0 0 1 0 0 1\n")
            f.write("2 0 1 0 0 0 0 1\n")
            f.write("1 0 1 0 0 0 0 1\n")
            f.write("1 0 0 0 1 1 0 0\n")
            f.write("1 1 1 1 1 1 1 1\n")
            f.write("6 7\n")
            f.close()

    # Create test case 2 (.map2.txt - no solution)
    if not (MAP_DIR / ".map2.txt").exists():
        with open(MAP_DIR / ".map2.txt", "w") as f:
            f.write("8 8\n")
            f.write("1 1 1 1 1 1 1 1\n")
            f.write("1 0 0 0 0 1 0 1\n")
            f.write("1 1 1 0 0 0 0 1\n")
            f.write("1 0 0 0 1 0 0 1\n")
            f.write("0 0 1 0 0 0 0 1\n")
            f.write("1 0 1 0 0 0 0 1\n")
            f.write("1 0 0 0 1 1 0 0\n")
            f.write("1 1 1 1 1 1 1 1\n")
            f.write("6 7\n")
            f.close()


def undo_test_case():
    # delete all map test cases
    (MAP_DIR / ".map1.txt").unlink()
    (MAP_DIR / ".map2.txt").unlink()


def test_dfs_lv1():
    # Generate test cases
    gen_test_case()

    # Check search algo run correctly in test case 1 (level 1)
    try:
        map, map_size, pacman_pos = read_map("map7.txt")
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
        pacman_path, path_len, ghosts_path, score = search_algo(
            TEST_ALGO_NAME, map, map_size, pacman_pos, 1
        )
    except Exception as e:
        print(e)
        print("Test failed")

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

    # Check search algo run correctly in test case 2 (level 1)
    # try:
    #     map, map_size, pacman_pos = read_map(".map4.txt")
    # except Exception as e:
    #     print("Test failed")

    # try:
    #     # Draw the initial state of the game
    #     pac_man_id, ghost_ids, food_ids, score_table_id = draw_pane(
    #         map, map_size, pacman_pos
    #     )
    # except Exception as e:
    #     print("Test failed")
    #     print(e)

    # try:
    #     pacman_path, path_len, ghosts_path, score = search_algo(
    #         TEST_ALGO_NAME, map, map_size, pacman_pos, 1
    #     )
    #     # real_score = 0
    #     # if score != real_score:
    #     #     print("Test failed")
    #     #     print(path, score)
    #     # else:
    #     #     print("Test passed")
    #     #     print(path, score)
    # except Exception as e:
    #     print(e)
    #     print("Test failed")
    
    # try:
    #     play_game(
    #         map_size,
    #         pac_man_id,
    #         ghost_ids,
    #         food_ids,
    #         score_table_id,
    #         pacman_path,
    #         ghosts_path,
    #         score,
    #         time_frame=0.3,
    #     )
    # except Exception as e:
    #     print(e)
    #     pass

    # Delete all map test cases
    undo_test_case()
