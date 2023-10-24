from app.settings import BASE_DIR
from app.utils.read_map import read_map
from app.search_algo import search_algo

MAP_DIR = BASE_DIR / 'app' / 'maps'

def test_bfs_lv1():
    # Create test case 1 (.map1.txt - have solution)
    if not (MAP_DIR / '.map1.txt').exists():
        with open(MAP_DIR / '.map1.txt', 'w') as f:
            f.write('5 5\n')
            f.write('1 1 1 1 1\n')
            f.write('1 0 0 0 1\n')
            f.write('2 0 1 0 1\n')
            f.write('1 0 1 0 0\n')
            f.write('1 1 1 1 1\n')
            f.write('3 4\n')
            f.close()

    try:
        map, map_size, pacman_pos = read_map('.map1.txt')
    except Exception as e:
        print("Test failed")

    # Check bfs run correctly in test case 1 (level 1)
    try:
        path, path_len, score = search_algo('bfs', map, map_size, pacman_pos, 1)
        if score == 1:
            print("Test passed")
        else:
            print("Test failed")
    except Exception as e:
        print(e)
        print("Test failed")

    # Create test case 2 (.map2.txt - no solution)
    if not (MAP_DIR / '.map2.txt').exists():
        with open(MAP_DIR / '.map2.txt', 'w') as f:
            f.write('5 5\n')
            f.write('1 1 1 1 1\n')
            f.write('1 0 0 0 1\n')
            f.write('0 0 1 0 1\n')
            f.write('1 0 1 0 0\n')
            f.write('1 1 1 1 1\n')
            f.write('3 4\n')
            f.close()

    try:
        map, map_size, pacman_pos = read_map('.map2.txt')
    except Exception as e:
        print("Test failed")

    # Check bfs run correctly in test case 2 (level 1)
    try:
        path, path_len, score = search_algo('bfs', map, map_size, pacman_pos, 1)
        if score == 0:
            print("Test passed")
        else:
            print("Test failed")

    except Exception as e:
        print(e)
        print("Test failed")
    