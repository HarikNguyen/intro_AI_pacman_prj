from app.constants import ALGO_NAME


def search_algo(algo_name, map, map_size, pacman_pos, level=1):
    """Search algorithm

    Args:
        algo_name (str): Search Algorithm name in lowercase (must define in constants.py (Algo_name list))
        map (_type_): _description_
        map_size (_type_): _description_
        pacman_pos (_type_): _description_
        level (int, optional): _description_. Defaults to 1.
    """

    # Check if the algorithm is defined in constants.py
    if algo_name not in ALGO_NAME:
        raise Exception("Algorithm name is not defined in constants.py")

    # Import the search algorithm
    from importlib import import_module

    algo = import_module(f"app.search_algo.level{level}.{algo_name}")

    algo_func = getattr(algo, algo_name)

    # Run the search algorithm
    return algo_func(map, map_size, pacman_pos)
