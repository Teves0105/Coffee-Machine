import time
def is_special_palindrome(inp_str, diff=0):
    # Base case when the length of the string is less or equal to 1
    if len(inp_str) <= 1:
        # Return boolean value
        return diff <= 2
    # Check the symmetry of the string
    if inp_str[0] != inp_str[-1]:
        diff += 1
    # If the diff > 2, then return false
    if diff > 2:
        return False
    # Recursive base with cutting the initial and the last elements in the string
    return is_special_palindrome(inp_str[1:-1], diff)

n = input()
print(is_special_palindrome(n))


#  Comment the execution time results
"""
Input: level
Recursive: True
Execution Time (Recursive):  0.000011 seconds

Input: dsfgefgsgr
Recursive: False
Execution Time (Recursive):  0.000011 seconds
"""