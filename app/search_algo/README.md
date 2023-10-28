## Các Level:

- Level 1: Pac-Man biết vị trí của thức ăn trên bản đồ và không có con quái nào ở xung quanh. Trên bản đồ chỉ có một thức ăn.
- Level 2: Các con quái đứng yên và không di chuyển xung quanh. Nếu Pac-Man và một con quái va chạm với nhau, trò chơi sẽ kết thúc. Trên bản đồ vẫn còn một thức ăn và Pac-Man biết vị trí của nó.
- Level 3: Tầm nhìn của Pac-Man bị hạn chế trong phạm vi ba bước gần nhất. Thức ăn bên ngoài phạm vi này sẽ không hiển thị với Pac-Man. Pac-Man chỉ có thể quét các ô liền kề trong phạm vi 8 ô x 3 ô. Có nhiều thức ăn được phân bố trên khắp bản đồ. Các con quái có thể di chuyển một bước theo bất kỳ hướng nào hợp lệ xung quanh vị trí ban đầu của chúng khi bắt đầu trò chơi. Cả Pac-Man và quái vật đều di chuyển một bước mỗi lượt.
- Level 4: Là một bản đồ kín, nơi các con quái không ngừng theo đuổi Pac-Man. Pac-Man phải thu thập càng nhiều thức ăn càng tốt trong khi tránh bị bất kỳ con quái nào bắt kịp. Các con quái có thể xuyên qua nhau. Cả Pac-Man và quái vật đều di chuyển một bước mỗi lượt và bản đồ chứa rất nhiều thức ăn.

## Các thuật toán:

- Level 1 & 2: DFS, BFS, UCS, A\*

## Cách triển khai thuật toán:

- Với mỗi level viết các file (module) là tên thuật toán (ví dụ: `dfs.py`, `bfs.py`, `ucs.py`, `a_star.py`) và phải định nghĩa tên thuật toán ở list (ALGO_NAME) trong file `app/constants/__init__.py`.
- Và trong file đó phải định nghĩa hàm trùng với tên file. Ví dụ: `def dfs(...):` trong file `dfs.py`.
- Hàm đó phải nhận đầu vào như sau `(map, map_size, pacman_pos)`
- Và đầu ra ở **level 1 & 2** phải là `path, len(path), score`

## Cách kiểm tra:

- Các bạn có thể tham khảo ở thư mục `/test`

## Require output:

- Output: path, len(path), ghost_paths, score
- path: List of matrix position of pacman (row_id, col_id)
- len(path): Length of **path**
- ghost_paths: List of list of matrix position of ghost (row_id, col_id). Ex: [{"mat_pos": (1, 2), "path": [(1, 2), (1, 3), (1, 4)]}, {"mat_pos": (2, 3), "path": [(2, 3), (2, 4), (2, 5)]}]
- score: Score of pacman
