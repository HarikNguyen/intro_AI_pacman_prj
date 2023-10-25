from app.settings import BASE_DIR
from app.utils.read_map import read_map
from app.graphic import draw_pane

MAP_DIR = BASE_DIR / 'app' / 'maps'

def gen_test_case():
    # Create test case 1 (.map1.txt - have solution)
    if not (MAP_DIR / '.map1.txt').exists():
        with open(MAP_DIR / '.map1.txt', 'w') as f:
            f.write('5 5\n')
            f.write('1 1 1 1 1\n')
            f.write('1 0 0 0 1\n')
            f.write('2 0 1 0 1\n')
            f.write('1 3 1 0 0\n')
            f.write('1 1 1 1 1\n')
            f.write('3 4\n')
            f.close()

def undo_test_case():
    # delete all map test cases
    (MAP_DIR / '.map1.txt').unlink()

def test_graphic():

    # Generate test cases
    gen_test_case()

    # Check bfs run correctly in test case 1 (level 1)
    
    try:
        map, map_size, pacman_pos = read_map('.map1.txt')
    except Exception as e:
        print("Test failed")

    # Draw the initial state of the game
    draw_pane(map, map_size, pacman_pos)
    
    # Undo test cases
    undo_test_case()