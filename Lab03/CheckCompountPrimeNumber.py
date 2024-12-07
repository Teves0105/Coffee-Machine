
def checkreverse(n: int) -> bool:
    temp = n
    new = 0
    while n!=0:
        new = new*10 + n%10
        n//=10
    if temp == new:
        return True
    else:
        return False

def checkprime(n: int) -> bool:
    count = 0
    for i in range(2,int(n**0.5)+1):
        if (n%i==0):
            count+=1
            while (n%i==0):
                n//=i
    if n>1: count+=1
    if count >= 3:
        return True
    else:
        return False
a,b = map(int,input().split())
for i in range(a,b+1):
    if checkreverse(i) and checkprime(i):
        print(i,end=' ')