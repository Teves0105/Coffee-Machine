def min_swaps_to_balance(s):
    """
    Hàm tính số lần hoán đổi tối thiểu để chuỗi dấu ngoặc trở thành hợp lệ.
    :param s: Chuỗi chứa các dấu ngoặc '(' và ')'.
    :return: Số lần hoán đổi tối thiểu.
    """
    balance = 0  # Đếm chênh lệch giữa số '(' và ')'
    swaps = 0    # Đếm số lần hoán đổi cần thiết

    # Duyệt qua từng ký tự trong chuỗi
    for char in s:
        if char == '(':
            balance += 1  # Tăng balance khi gặp '('
        else:  # char == ')'
            balance -= 1  # Giảm balance khi gặp ')'

        # Nếu balance < 0, có quá nhiều ')', cần hoán đổi
        if balance < 0:
            swaps += 1      # Tăng số lần hoán đổi
            balance = 0     # Đặt lại balance về 0 sau khi hoán đổi
    return swaps

# Phần kiểm tra và chạy chương trình
if __name__ == "__main__":
    # Nhập chuỗi dấu ngoặc từ người dùng
    s = input("Nhập chuỗi dấu ngoặc: ")
    # Gọi hàm và in kết quả
    result = min_swaps_to_balance(s)
    print(f"Số lần hoán đổi tối thiểu để chuỗi hợp lệ: {result}")
