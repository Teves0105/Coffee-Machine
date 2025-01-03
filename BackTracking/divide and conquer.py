import math

# Hàm tính khoảng cách giữa hai điểm
def distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

# Hàm tìm khoảng cách nhỏ nhất bằng cách duyệt cặp điểm gần nhau ở biên
def closest_in_strip(strip, d_min):
    min_dist = d_min
    n = len(strip)
    # Duyệt từng cặp điểm trong strip (theo trật tự y)
    for i in range(n):
        for j in range(i + 1, n):
            if (strip[j][1] - strip[i][1]) >= min_dist:
                break
            min_dist = min(min_dist, distance(strip[i], strip[j]))
    return min_dist

# Hàm tìm khoảng cách nhỏ nhất bằng chia để trị
def closest_pair_rec(points_sorted_x, points_sorted_y):
    n = len(points_sorted_x)

    # Điều kiện dừng khi số điểm nhỏ
    if n <= 3:
        min_dist = float('inf')
        for i in range(n):
            for j in range(i + 1, n):
                min_dist = min(min_dist, distance(points_sorted_x[i], points_sorted_x[j]))
        return min_dist

    # Chia các điểm thành hai nửa
    mid = n // 2
    mid_point = points_sorted_x[mid]

    left_x = points_sorted_x[:mid]
    right_x = points_sorted_x[mid:]

    left_y = list(filter(lambda p: p[0] <= mid_point[0], points_sorted_y))
    right_y = list(filter(lambda p: p[0] > mid_point[0], points_sorted_y))

    # Tìm khoảng cách nhỏ nhất ở hai nửa
    d_left = closest_pair_rec(left_x, left_y)
    d_right = closest_pair_rec(right_x, right_y)
    d_min = min(d_left, d_right)

    # Kiểm tra khoảng cách nhỏ nhất ở dải biên
    strip = [p for p in points_sorted_y if abs(p[0] - mid_point[0]) < d_min]
    d_strip = closest_in_strip(strip, d_min)

    return min(d_min, d_strip)

# Hàm chính
def closest_pair(points):
    points_sorted_x = sorted(points, key=lambda p: p[0])
    points_sorted_y = sorted(points, key=lambda p: p[1])
    return closest_pair_rec(points_sorted_x, points_sorted_y)

# Ví dụ
points = [(2, 3), (12, 30), (40, 50), (5, 1), (12, 10), (3, 4)]
result = closest_pair(points)
print("Khoảng cách nhỏ nhất giữa hai điểm:", result)
