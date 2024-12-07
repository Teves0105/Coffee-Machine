def generate_pascals_triangle(n):
    triangle = []

    for i in range(n):
        row = [1] * (i + 1)  # Tạo một hàng mới với toàn bộ phần tử là 1

        # Tính giá trị cho các phần tử giữa của hàng
        for j in range(1, i):
            row[j] = triangle[i - 1][j - 1] + triangle[i - 1][j]

        triangle.append(row)

    return triangle

# Hàm hiển thị tam giác Pascal
def print_pascals_triangle(triangle):
    for row in triangle:
        print(' '.join(map(str, row)).center(2*n))

# Nhập số hàng của tam giác Pascal
n = int(input("Nhập số hàng của tam giác Pascal: "))

# Tạo tam giác Pascal và hiển thị
triangle = generate_pascals_triangle(n)
print_pascals_triangle(triangle)