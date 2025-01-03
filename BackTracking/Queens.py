# Hàm kiểm tra vị trí (row, col) có an toàn để đặt quân hậu không
def is_safe(board, row, col, n):
    # Kiểm tra cột
    for i in range(row):
        if board[i][col] == 1:
            return False

    # Kiểm tra đường chéo trên bên trái
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    # Kiểm tra đường chéo trên bên phải
    for i, j in zip(range(row, -1, -1), range(col, n)):
        if board[i][j] == 1:
            return False

    return True

# Hàm chính giải bài toán 8 quân hậu
def solve_n_queens(board, row, n):
    # Nếu đã đặt đủ n quân hậu, trả về True
    if row >= n:
        return True

    # Thử đặt quân hậu ở từng cột trong hàng hiện tại
    for col in range(n):
        if is_safe(board, row, col, n):
            # Đặt quân hậu
            board[row][col] = 1

            # Đệ quy đặt quân hậu ở hàng tiếp theo
            if solve_n_queens(board, row + 1, n):
                return True

            # Nếu không thành công, quay lui
            board[row][col] = 0

    # Nếu không thể đặt quân hậu ở bất kỳ cột nào, trả về False
    return False

# Hàm in bảng cờ
def print_board(board):
    for row in board:
        print(" ".join("Q" if cell == 1 else "." for cell in row))

# Kích thước bàn cờ (8x8)
n = 8
board = [[0 for _ in range(n)] for _ in range(n)]

if solve_n_queens(board, 0, n):
    print("Bài toán có lời giải:")
    print_board(board)
else:
    print("Không tìm được lời giải.")
