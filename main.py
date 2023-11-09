import argparse
from app.settings import BASE_DIR
from app.constants import ALGO_NAME
from app.utils.read_map import read_map
from app.search_algo import search_algo
from app.graphic import draw_pane, play_game
from app.utils.find_max_score import find_max_score

# Define the parser
def config(parser):
    parser.add_argument("--lv", type=int, default=1, help="Level")
    parser.add_argument(
        "--build_in_map", type=str, default="map1.txt", help="Build-in Map"
    )
    parser.add_argument("--map", type=str, default="", help="Map")
    parser.add_argument("--algo", type=str, default="ucs", help="Algorithm")
    return parser


# Define the main function
def main(args):
    # Get map path
    map_path = get_map_path(args.map, args.build_in_map)

    # Read map
    try:
        map, map_size, pacman_pos = read_map(map_path)
    except:
        print("Error: Cannot read map")
        return

    # validate algo name
    algo_name = args.algo

    is_valid_algo_name = validate_algo_name(algo_name)
    if not is_valid_algo_name:
        print("Invalid algo name")
        return

    # Draw pane
    try:
        pacman_id, ghost_ids, food_ids, score_table_id = draw_pane(
            map, map_size, pacman_pos
        )
    except:
        print("Error: Cannot draw pane")
        return

    # Get paths by search algorithm
    try:
        if args.lv == 4:
            path, ghost_paths = search_algo(
                algo_name, map, map_size, pacman_pos, args.lv
            )
            score = find_max_score(map)
        else:
            path, path_len, ghost_paths, score = search_algo(
                algo_name, map, map_size, pacman_pos, args.lv
            )
    except:
        print("Error: Cannot get paths by search algorithm")
        return

    # Play game
    # try:
    play_game(
        map_size,
        pacman_id,
        ghost_ids,
        food_ids,
        score_table_id,
        pacman_path=path,
        ghost_paths=ghost_paths,
        extract_score=score,
        time_frame=0.2,
    )
    # except:
    #     print("Error: Cannot play game")
    #     return


def get_map_path(map_path, build_in_map):
    # if map_path not having
    if map_path == None or map_path == "":
        # return build_in_map
        return build_in_map
    # else
    else:
        # return map_path
        return map_path


def validate_algo_name(algo_name):
    # validate algo name
    return algo_name in ALGO_NAME


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Pacman")
    parser = config(parser)
    args = parser.parse_args()
    main(args)
