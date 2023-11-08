import os
import sys

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))

from test_read_input import test_read_input
from test_bfs_lv1 import test_bfs_lv1
from test_bfs_lv2 import test_bfs_lv2
from test_dfs_lv1 import test_dfs_lv1
from test_dfs_lv2 import test_dfs_lv2
from test_a_star_lv1 import test_a_star_lv1
from test_a_star_lv2 import test_a_star_lv2
from test_graphic import test_graphic
from test_ucs_lv1 import test_ucs_lv1
from test_ucs_lv2 import test_ucs_lv2
from test_ucs_lv3 import test_ucs_lv3
from test_graphic_v2 import test_graphic_v2
from test_alpha_beta import test_alpha_beta

if __name__ == "__main__":
    # test_read_input()
    # test_bfs_lv1()
    # test_dfs_lv1()
    # test_ucs_lv1()
    # test_a_star_lv1()
    # test_bfs_lv2()
    # test_dfs_lv2()
    # test_ucs_lv2()
    # test_ucs_lv3()
    # test_a_star_lv2()
    test_alpha_beta()
    # test_graphic()
    # test_graphic_v2()
