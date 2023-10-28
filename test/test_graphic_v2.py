from app.settings import BASE_DIR
from app.utils.read_map import read_map
from app.graphic import draw_pane, play_game
from app.search_algo import search_algo

MAP_DIR = BASE_DIR / "app" / "maps"
SEARCH_ALGO_EXP = "bfs"


def gen_test_case():
    # Create test case 1 (.map1.txt - have solution)
    if not (MAP_DIR / ".map1.txt").exists():
        with open(MAP_DIR / ".map1.txt", "w") as f:
            f.write("10 20\n")
            f.write("1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1\n")
            f.write("1 0 1 0 1 0 1 0 1 0 1 1 1 0 1 0 1 0 1 1 \n")
            f.write("1 0 0 0 0 0 1 0 1 0 1 1 1 0 1 0 0 0 1 1\n")
            f.write("1 1 0 1 1 0 1 0 1 0 0 0 0 0 1 0 1 0 0 0\n")
            f.write("1 0 0 1 1 0 0 0 1 0 1 1 1 0 1 0 1 0 1 2\n")
            f.write("1 1 0 1 1 0 3 0 1 0 1 1 1 0 1 0 1 0 1 1\n")
            f.write("1 0 0 1 1 0 1 0 1 0 0 0 0 0 1 0 1 0 1 1\n")
            f.write("1 1 0 0 0 0 1 0 1 0 1 1 1 0 1 0 1 0 1 1\n")
            f.write("1 0 2 3 1 0 1 0 0 0 1 0 0 2 0 0 0 0 1 1\n")
            f.write("1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1\n")
            f.write("1 1\n")
            f.close()


def undo_test_case():
    # delete all map test cases
    (MAP_DIR / ".map1.txt").unlink()


def test_graphic_v2():

    # Generate test cases
    gen_test_case()

    # Check bfs run correctly in test case 1 (level 1)

    try:
        map, map_size, pacman_pos = read_map(".map1.txt")
    except Exception as e:
        print("Test failed")
        print(e)

    try:
        # Example search algo
        path, path_len, ghost_paths, score = search_algo(
            SEARCH_ALGO_EXP, map, map_size, pacman_pos, 2
        )
    except Exception as e:
        print("Test failed")
        print(e)

    try:
        # Draw the initial state of the game
        pac_man_id, ghost_ids, food_ids, score_table_id = draw_pane(map, map_size, pacman_pos)
    except Exception as e:
        print("Test failed")
        print(e)

    try:
        play_game(
            map_size,
            pac_man_id,
            ghost_ids,
            food_ids,
            score_table_id,
            path,
            ghost_paths,
            score,
            time_frame=0.3,
        )
    except Exception as e:
        print(e)
        pass

    # Undo test cases
    undo_test_case()
