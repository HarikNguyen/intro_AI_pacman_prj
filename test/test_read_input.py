from app.settings import BASE_DIR
from app.utils.read_map import read_map

MAP_DIR = BASE_DIR / 'app' / 'maps'

def test_read_input():
    # Create test case
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
        print("Test passed")
    except Exception as e:
        print("Test failed")
