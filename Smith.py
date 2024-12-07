n = int(input())

def totaldigits(n: int) -> int:
    sum = 0
    while n!=0:
        sum+=n%10
        n//=10
    return sum
def prime(n:int) -> bool:
    if (n<2):
        return False
    for i in range(2,int(n**0.5)+1):
        if (n%i==0):
            return False
    return True

def checkSmith(n: int) -> bool:
    sum = 0
    k = n
    for i in range(2, int(n ** 0.5) + 1):
        if (n % i == 0):
            while (n % i == 0):
                sum+= totaldigits(i)
                n //= i
    if n>1: sum+=totaldigits(n)
    if sum == totaldigits(k):
        return True
    else:
        return False



if checkSmith(n) and prime(n) == False: print('1')
else: print('0')
