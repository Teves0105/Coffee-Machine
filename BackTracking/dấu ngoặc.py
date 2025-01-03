def min_swaps_to_balance(s):
    imbalance = 0  # Số lượng ngoặc đóng `]` mất cân bằng
    swap_count = 0  # Số phép hoán đổi cần thiết
    open_count = 0  # Số lượng ngoặc mở `[` đang chờ ghép

    for char in s:
        if char == '[':
            open_count += 1
            # Nếu có mất cân bằng, ta sẽ khôi phục bằng ngoặc mở này
            if imbalance > 0:
                swap_count += imbalance
                imbalance -= 1  # Mất cân bằng giảm đi do đã ghép được
        elif char == ']':
            imbalance += 1  # Mất cân bằng tăng lên do gặp ngoặc đóng
            if open_count > 0:
                open_count -= 1  # Ghép ngoặc mở trước đó, không cần hoán đổi
                imbalance -= 1

    return swap_count
