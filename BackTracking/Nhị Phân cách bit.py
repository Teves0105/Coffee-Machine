def print_solution(x):
    for value in x:
        print(value, end="")
    print()  # In thêm một dòng mới sau khi in xong

def TRY(x, n, k):
    for v in range(2):
        if k > 0 and v + x[k - 1] == 2:
            continue
        x[k] = v
        if k == n - 1:
            print_solution(x)
        else:
            TRY(x, n, k + 1)

def main():
    n = 5
    x = [0] * n  # Khởi tạo mảng x với tất cả phần tử là 0
    TRY(x, n, 0)

if __name__ == "__main__":
    main()
