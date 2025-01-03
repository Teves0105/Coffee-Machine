

n = int(input())

a = [0]*n
def Try(k):

    if k == n:
        print(a)
    else:
        for element in range(2):
            a[k] = element
            Try(k+1)
            a[k]= 0

Try(0)