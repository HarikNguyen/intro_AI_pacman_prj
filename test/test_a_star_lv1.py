from app.settings import BASE_DIR
from app.utils.read_map import read_map
from app.search_algo import search_algo

MAP_DIR = BASE_DIR / "app" / "maps"
TEST_ALGO_NAME = "a_star"


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


def test_a_star_lv1():
    # Generate test cases
    gen_test_case()

    # Check search algo run correctly in test case 1 (level 1)
    try:
        map, map_size, pacman_pos = read_map(".map1.txt")
    except Exception as e:
        print("Test failed")

    try:
        path, path_len, ghost_paths, score = search_algo(
            TEST_ALGO_NAME, map, map_size, pacman_pos, 1
        )
        real_score = 31
        if score != real_score:
            print("Test failed")
            print(path, score)
        else:
            print("Test passed")
            print(path)
    except Exception as e:
        print(e)
        print("Test failed")

    # Check search algo run correctly in test case 2 (level 1)
    try:
        map, map_size, pacman_pos = read_map(".map2.txt")
    except Exception as e:
        print("Test failed")

    try:
        path, path_len, ghost_paths, score = search_algo(
            TEST_ALGO_NAME, map, map_size, pacman_pos, 1
        )
        real_score = 0
        if score != real_score:
            print("Test failed")
            print(path, score)
        else:
            print("Test passed")
            print(path)

    except Exception as e:
        print(e)
        print("Test failed")

    # Delete all map test cases
    undo_test_case()
