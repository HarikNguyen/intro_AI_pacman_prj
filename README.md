# Project

## Description

Đây là project môn học Trí tuệ nhân tạo. Chủ đề Search Algorithms (Pacman project).

## Cấu trúc thư mục

```
.
├── app
│   ├── constants/
│   │   ├── __init__.py # Các hằng số, các tên thuật toán
|   |-- graphic/ # Các file liên quan đến giao diện
|   |-- maps/ Chứa các file map (tên file map có dạng map<index>.txt)
|   |-- search_algo/ # Các thuật toán tìm kiếm
|   |-- |-- level1/ # Các file triển khai thuật toán ở level 1
|   |-- |-- level2/ # Các file triển khai thuật toán ở level 2
|   |-- |-- level3/ # Các file triển khai thuật toán ở level 3
|   |-- |-- level4/ # Các file triển khai thuật toán ở level 4
|   |-- |-- __init__.py # Chứa hàm search_algo(algo_name, map, map_size, pacman_pos, level = 1) để gọi các thuật toán (interface)
|   |-- utils/ # Các hàm tiện ích (ví dụ: đọc file map, ...)
|   |-- settings/ # Các file cấu hình (ví dụ: base_url, ...)
|   main.py # File chính (file thực thi toàn bộ project)
├── test/ # Các file test
├── README.md
|-- .gitignore # File loại bỏ các file không cần thiết khi commit
|-- venv/ # Virtual environment (chứa các thư viện cần thiết khi thiết lập môi trường virtual env)
|-- Pipfile # File chứa các thư viện cần thiết khi thiết lập môi trường virtual env (dùng pipenv để cài đặt)
|-- Pipfile.lock # File chứa các thư viện cần thiết khi thiết lập môi trường virtual env (dùng pipenv để cài đặt)

```

## Khởi chạy môi trường ảo venv

- Windows (cmd)

```
> Set-ExecutionPolicy RemoteSigned -Scope Process
> py -3 -m venv venv or py -3 -m virtualenv venv
> source venv/Scripts/activate
> pip install pipenv
> pipenv install
```

- Linux

```
$ python3 -m venv venv or python -m virtualenv venv (if python ~ python3)
$ source venv/bin/activate
$ pip install pipenv
$ pipenv install
```

## Yêu cầu hiện tại (cập nhật ngày 25/10/2023)

- Triển khai 4 thuật toán cho level 1 & 2 (DFS, BFS, UCS, A\*)
- Triển khai graphical

## Yêu cầu sử dụng git theo gitflow

- Các branch chính: master (main)
- Các branch phụ: feat/<action>, fix/<action>, ...
- Các branch phụ sẽ được merge vào master khi hoàn thành hay fix lỗi 1 chức năng nào đó (ví dụ feat/dfs, fix/dfs, ...) (sau khi tạo pull request và được review - accept)
