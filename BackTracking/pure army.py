def is_safe(bishops, row, col, n):
    """
    Kiểm tra xem có thể đặt quân tượng tại (row, col) hay không.
    """
    for r, c in bishops:
        # Kiểm tra đường chéo chính và đường chéo phụ
        if abs(r - row) == abs(c - col):
            return False
    return True


def solve_bishops(n, k, row, bishops, solutions):
    """
    Thuật toán quay lui để tìm tất cả cách đặt k quân tượng trên bàn cờ nxn.
    """
    # Nếu đã đặt đủ k quân tượng, lưu lại cách xếp
    if len(bishops) == k:
        solutions.append(bishops[:])
        return

    # Nếu đã duyệt hết bàn cờ, dừng
    if row >= n:
        return

    for col in range(n):
        # Kiểm tra xem có thể đặt quân tượng tại (row, col) hay không
        if is_safe(bishops, row, col, n):
            # Đặt quân tượng tại (row, col)
            bishops.append((row, col))
            # Đệ quy đặt quân tượng tiếp theo ở hàng tiếp theo
            solve_bishops(n, k, row + 1, bishops, solutions)
            # Backtrack: Gỡ quân tượng vừa đặt
            bishops.pop()

    # Không đặt quân tượng tại hàng này, thử hàng tiếp theo
    solve_bishops(n, k, row + 1, bishops, solutions)


def print_solutions(solutions, n):
    """
    In tất cả các cách xếp quân tượng.
    """
    for solution in solutions:
        board = [['.' for _ in range(n)] for _ in range(n)]
        for r, c in solution:
            board[r][c] = 'B'
        for row in board:
            print(' '.join(row))
        print()


# Nhập kích thước bàn cờ và số lượng quân tượng
n = 4  # Kích thước bàn cờ (nxn)
k = 2  # Số lượng quân tượng cần đặt

# Tìm tất cả các cách xếp
solutions = []
solve_bishops(n, k, 0, [], solutions)

# In kết quả
print(f"Tìm được {len(solutions)} cách xếp:")
print_solutions(solutions, n)
