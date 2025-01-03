


n = int(input())

a = [0]*n
visited = [0]*(n+1)

def Try(k):
    if k == n:
        print(a)
    else:
        for y in range(1,n+1):
            if not visited[y]:
                a[k] = y
                visited[y] = True
                Try(k+1)
                a[k] = 0
                visited[y]= False

Try(0)