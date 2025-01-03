N = 5  # Kích thước của ma trận

# Hàm in giải pháp
def print_solution(sol):
    for i in range(N):
        for j in range(N):
            print(sol[i][j], end=" ")
        print()

# Hàm kiểm tra tính hợp lệ của ô (x, y)
def is_safe(maze, x, y):
    if x >= 0 and x < N and y >= 0 and y < N and maze[x][y] == 1:
        return True
    return False

# Hàm đệ quy giải quyết bài toán
def solve_maze_util(maze, x, y, sol):
    # Nếu đã đến ô đích, đánh dấu ô này và trả về True
    if x == N - 1 and y == N - 1 and maze[x][y] == 1:
        sol[x][y] = 1
        return True

    # Kiểm tra nếu ô (x, y) hợp lệ
    if is_safe(maze, x, y):
        # Nếu ô này đã được đánh dấu là phần của đường đi, trả về False
        if sol[x][y] == 1:
            return False

        # Đánh dấu ô (x, y) là phần của đường đi
        sol[x][y] = 1

        # Di chuyển theo các hướng: xuống, phải, lên, trái
        if solve_maze_util(maze, x + 1, y, sol):
            return True
        if solve_maze_util(maze, x, y + 1, sol):
            return True
        if solve_maze_util(maze, x - 1, y, sol):
            return True
        if solve_maze_util(maze, x, y - 1, sol):
            return True

        # Nếu không thể đi tiếp, đánh dấu lại ô (x, y) là không phải phần của đường đi
        sol[x][y] = 0
        return False

    return False

# Hàm chính để bắt đầu giải bài toán
def solve_maze(maze):
    sol = [[0 for _ in range(N)] for _ in range(N)]  # Khởi tạo ma trận giải pháp

    # Nếu không có đường đi, in ra thông báo và trả về False
    if not solve_maze_util(maze, 0, 0, sol):
        print("Solution doesn't exist")
        return False

    # In ra ma trận giải pháp nếu tìm được đường đi
    print_solution(sol)
    return True

# Mê cung (1 là có thể đi, 0 là không thể đi)
maze = [
    [1, 0, 0, 0, 0],
    [1, 1, 0, 1, 0],
    [0, 1, 0, 0, 0],
    [1, 1, 1, 1, 0],
    [0, 0, 0, 1, 1]
]

# Gọi hàm chính để giải quyết bài toán
solve_maze(maze)
