import time
def sum_of_digits ( num , position =0) :
    # Base case when position out of range of the length of the num
    if position >= len(str(num)):
        return 0
    else:
    # Recursive case
        return int(str(num)[position]) + sum_of_digits(num, position + 2)


n = int(input())
n = abs(n)
convert_string = str(n)
n = int(convert_string[::-1])
print(sum_of_digits(n))

#  Comment the execution time results
"""
Input: 2222222
8
Recursive: 8
Execution Time (Recursive):  0.000017 seconds

Input: -244
Recursive: 6
Execution Time (Recursive):  0.000010 seconds
"""