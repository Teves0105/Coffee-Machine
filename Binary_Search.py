def binarySearch(a, n, x):
     left = 0
     right = n - 1
     res = -1
     while left <= right:
         mid = (left + right)//2
         if a[mid] < x:
             left = mid +1
             res = mid
         else:
             right = mid - 1
     return res + 1


n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

b.sort()
for i in range(n):
    print(binarySearch(b, m, a[i]),end=' ')
