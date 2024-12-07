import time
def print_pattern_sequential(n):
    for i in range(n):
        for j in range(i+1):
            print('*',end='')
        print()
def print_pattern_recursive(n, row = 1):
    # Base case when row larger than n
    if row > n:
        return
    print('*' * row)
    # Recursive case
    print_pattern_recursive(n, row+1)


n = int(input())
# Print the result
print("Sequential:")
print_pattern_sequential(n)
print("Recursive:")
print_pattern_recursive(n)

#  Comment the execution time results
"""
Input: 5
Sequential:
*
**
***
****
*****
Execution Time (Sequential):  0.000044 seconds
Recursive:
*
**
***
****
*****
Execution Time (Recursive):  0.000022 seconds

Input: 10
Sequential:
*
**
***
****
*****
******
*******
********
*********
**********
Execution Time (Sequential):  0.000175 seconds
Recursive:
*
**
***
****
*****
******
*******
********
*********
**********
Execution Time (Recursive):  0.000037 seconds
"""