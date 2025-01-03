def printSolution(x, n):
    for k in range(n):
        print(x[k], end=' ')
    print()  # Add a newline after printing the solution.

def Try(x, n, k):
    for v in range(2):
        x[k] = v
        if k == n - 1:
            printSolution(x, n)
        else:
            Try(x, n, k + 1)

n = 5
x = [0] * n  # Initialize a list of size `n` filled with zeros.

Try(x, n, 0)


