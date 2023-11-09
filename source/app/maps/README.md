This folder contains map representations (map{id}.txt)

## Map format

The map is a text file with the following format:

- The first line contains two integers N x M, indicating the size of the map.
- The next N lines represent the N x M map matrix. Each line contains M integers. The value at position [i, j] (row i, column j) determines the presence of a wall, food, or monster. A value of 1 represents a wall, 2 represents food, 3 represents a monster, and 0 represents an empty path.
- The last line contains a pair of integers indicating the indices of Pacman's position (indices start from 0).

## Note

- This folder must contain at least 5 map file.
