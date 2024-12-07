def prime(n: int) -> bool:
    if (n<2): return False
    for i in range(2,int(n**0.5)+1):
        if (n%i==0):
            return False
    return True

T = int(input())

for i in range(T):
    n = int(input())
    for j in range(2,n//2+1):
        if prime(j) and prime(n-j):
            print(f"{j} {n-j}")