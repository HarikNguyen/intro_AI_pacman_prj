import os
import sys

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))

from test_read_input import test_read_input
from test_bfs_lv1 import test_bfs_lv1
from test_bfs_lv2 import test_bfs_lv2
from test_graphic import test_graphic
from test_graphic_w_ghost import test_graphic_w_ghost

if __name__ == "__main__":
    # test_read_input()
    # test_bfs_lv1()
    # test_bfs_lv2()
    # test_graphic()
    test_graphic_w_ghost()
