# Your code for the problem
import time
f = []
def fibonacci_sequential(n):
    """ Calculates fibonacci iteratively."""
    if n == 0: return 0
    elif n == 1: return 1
    else:
        f = [0]*(n+1)
        f[0] = 0
        f[1] = 1
        for i in range(2,n+1):
            f[i] = f[i-1] + f[i-2]
    return f[n]
def fibonacci_recursive(n):
    """Calculates fibonacci recursively."""
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci_recursive(n-1) + fibonacci_recursive(n-2)


n = int(input())

print(f"Sequential: {fibonacci_sequential(n)}")
print(f"Recursive: {fibonacci_recursive(n)}")


# Comment the execution time results
"""
Input: 5
Sequential: 5
Execution Time (Sequential): 0.00005220 seconds
Recursive: 5
Execution Time (Sequential): 0.00001020 seconds


Input: 10
Sequential: 55
Execution Time (Sequential): 0.00005750 seconds
Recursive: 55
Execution Time (Sequential): 0.00002480 seconds
"""