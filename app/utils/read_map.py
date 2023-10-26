from ..settings import BASE_DIR

MAP_DIR = BASE_DIR / "app" / "maps"


def is_pacman_pos_valid(map, pacman_pos):
    return map[pacman_pos[0]][pacman_pos[1]] == 0


def is_map_valid(map):
    # all rows must have the same length
    for row in range(len(map)):
        if len(map[0]) != len(map[row]):
            return False
    # map doesn't have any invalid value (!= 0, 1, 2, 3)
    for row in range(len(map)):
        for col in range(len(map[row])):
            if map[row][col] not in [0, 1, 2, 3]:
                return False
    return True


def read_map(map_name):
    map_file = MAP_DIR / map_name
    with open(map_file) as f:
        # read map size
        map_size = f.readline().split()
        # transform map size to int
        for i in range(len(map_size)):
            map_size[i] = int(map_size[i])

        # define map
        map = []
        # read map
        for row in range(int(map_size[0])):
            map.append(f.readline().split())
        # transform map to int values
        for row in range(int(map_size[0])):
            for col in range(int(map_size[1])):
                map[row][col] = int(map[row][col])
        # check map constraints
        if is_map_valid(map) == False:
            raise Exception("Invalid map")

        # read pacman position
        pacman_pos = f.readline().split()
        # transform pacman position to int
        for i in range(len(pacman_pos)):
            pacman_pos[i] = int(pacman_pos[i])
        # check pacman constraints
        if is_pacman_pos_valid(map, pacman_pos) == False:
            raise Exception("Invalid pacman position")

        # return map and pacman position
        return map, tuple(map_size), tuple(pacman_pos)
