"""
Definite the function to create 2D array where each inner array contains two elements:
the index and the positive number  from the input list.
"""
def enumerate_positive(numbers):
    # Create the empty list, it will be the result
    List = []
    for i in range(len(numbers)):
        # Check if the element is positive number, if it is true, the List will append the index and the value
        if numbers[i] > 0:
            List.append([i, numbers[i]])
    return List

# Input the number of element and the list
n = int(input())
numbers = list(map(int, input().split()))

# Print the result
print(enumerate_positive(numbers))