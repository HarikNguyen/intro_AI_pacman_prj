
import os
import sys

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))

# from .test_read_input import test_read_input
from test_bfs_lv1 import test_bfs_lv1

if __name__ == '__main__':
    # test_read_input()
    test_bfs_lv1()
