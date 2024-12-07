"""
 Define the function which find the smallest positive integer
 that is not present in the list through using for-loop
"""
def smallest_integer_for(arr):
    # Set a variable result = 1
    result = 1
    # Sort the list to find the result easily
    arr.sort()
    # Consider all the elements in the list
    for i in range(len(arr)):
        """ If the value of arr[i] is equal to result, 
        then increase the value for result
        """
        if result == arr[i]:
            result += 1
    return result
"""
 Define the function which find the smallest positive integer
 that is not present in the list through using while-loop
"""
def smallest_integer_while(arr):
    result = 1
    arr.sort()
    i = 0
    while i < len(arr):
        """ 
        If the value of arr[i] is equal to result, 
        then increase the value for result
        """
        if result == arr[i]:
            result +=1
        # increment for i to run the while-loop
        i+=1
    return result

# Input a list
arr = list(map(int, input().split()))

# Print the result
print(smallest_integer_for(arr))
print(smallest_integer_while(arr))