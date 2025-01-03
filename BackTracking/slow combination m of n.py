n,m = map(int, input().split())
a = [0]*m
def Try(k):
    if k == m:
        print(a)
    else:
        for y in range(a[max(0,k-1)]+1, n):
            a[k] = y
            Try(k+1)
            a[k] = 0
Try(0)

