n = int(input("Enter the number of terms (n): "))
sum_target = int(input("Enter the target sum: "))

a = [0]*n

current_sum = 0

def Try(k):
    global current_sum
    if k == n:
        if current_sum == sum_target:
            print(" + ".join(map(str, a[:k])), "=", sum_target)

    else:
        for y in range(1, sum_target - current_sum - (n - k - 1) + 1):
            a[k] = y
            current_sum += y
            Try(k+1)
            current_sum -= y


Try(0)