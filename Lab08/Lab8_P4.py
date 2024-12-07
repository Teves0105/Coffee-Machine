
# Input n, list, k respectively
n = int(input())
arr = list(map(int, input().split()))
k = int(input())

# Create the max_result valuable and assign it the value of -1
max_result = -1
# Consider the subarray
for index in range(n - k + 1):
    # Track the temp_list as a subarray
    temp_list = arr[index: index + k]
    # new_set will count the distinct number in temp_list
    new_set = set(temp_list)
    # Comparison to find the maximum distinct elements
    if max_result < len(new_set):
        max_result = len(new_set)

# Print to the screen
print(max_result)