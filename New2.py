# Hàm so sánh dựa trên giá trị tuyệt đối
def sum_character(n):
    total =0
    while n:
        total +=n%10
        n//=10
    return total
def cmp_abs(x):
    return (sum_character(x),x)

# Nhập n và danh sách a
n = int(input("Nhập số phần tử: "))
a = list(map(int, input("Nhập các phần tử: ").split()))

# Sắp xếp ổn định theo giá trị tuyệt đối giảm dần
a.sort(key=cmp_abs)

# In ra kết quả
print(" ".join(map(str, a)))