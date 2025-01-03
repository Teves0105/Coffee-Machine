def merge_sort(array):
    # Điều kiện dừng: Nếu mảng có 1 hoặc không có phần tử, nó đã được sắp xếp
    if len(array) <= 1:
        return array

    # Chia mảng làm đôi
    mid = len(array) // 2
    left_half = merge_sort(array[:mid])
    right_half = merge_sort(array[mid:])

    # Trộn hai nửa đã sắp xếp
    return merge(left_half, right_half)

def merge(left, right):
    result = []  # Mảng lưu trữ kết quả đã sắp xếp
    i = j = 0

    # So sánh từng phần tử của hai nửa và trộn vào mảng kết quả
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    # Thêm các phần tử còn lại (nếu có) vào mảng kết quả
    result.extend(left[i:])
    result.extend(right[j:])
    return result

# Ví dụ:
array = [7, 3, 2, 16, 24, 4, 11, 9]
sorted_array = merge_sort(array)
print("Mảng sau khi sắp xếp:", sorted_array)
