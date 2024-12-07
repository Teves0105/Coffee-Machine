
# Definite the binary search to tackle this problem
def binary_search(given_unsorted_list, k):
    # Find the lowest value and highest value
    low = min(given_unsorted_list)
    high = max(given_unsorted_list)
    # Create a count_list that counting the occurrence of each element
    count_list = [0 for _ in range(-101,101)]
    # Transform the value of k
    k = len(given_unsorted_list) - k + 1

    # Increment the count_list
    for value in given_unsorted_list:
        count_list[value] +=1

    for i in range(low,high+1):
        # if the element still exist in the list
        if count_list[i] != 0:
            # Increase the value of appearance
            count_list[i] = count_list[i-1] + count_list[i]
        else:
            # Assign to the before value
            count_list[i] = count_list[i-1]
    # Use binary search to find the suitable position
    while low <= high:
        mid = (low+high)//2
        # if the find process is successful
        if k == count_list[mid]:
            # In case there are many value of k in the count_list, it needed to find the lowest position
            while count_list[mid-1] == k:
                mid -= 1
            return mid
        # If the occurrence of this position less than k
        if k > count_list[mid]:
            # Change the value for low
            low = mid + 1
        else:
            # Otherwise, change the value for high
            high = mid - 1

    return -1
# Input
unsorted_list = list(map(int, input().split()))
k = int(input())
# Print the final result
print(binary_search(unsorted_list,k))

