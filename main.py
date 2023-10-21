import argparse

# Define the parser

def config(parser):
    parser.add_argument('--lv', type=int, default=1, help='Level')
    parser.add_argument('--map', type=str, default='map1.txt', help='Map')

    return parser

def main(args):
    print(args)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Pacman')
    parser = config(parser)
    args = parser.parse_args()
    main(args)