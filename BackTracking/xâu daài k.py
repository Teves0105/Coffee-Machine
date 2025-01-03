def backtracking(array, k, current_length):
    if current_length == k:
        print("".join(array[:k]))  # In ra xâu độ dài k
    else:
        for char in characters:
            array[current_length] = char
            backtracking(array, k, current_length + 1)


# Input dữ liệu
characters = list("ABCDEFGH")  # Các ký tự từ chuỗi gốc
k = 5  # Độ dài xâu mong muốn
array = [''] * k  # Mảng tạm để lưu xâu hiện tại

# Bắt đầu backtracking
backtracking(array, k, 0)
