
# Definite the function that create a list of a single list of the given input list
def initialize_chunks(number_list):
    return [[x] for x in number_list]

# Definite the function that merge two sublist to a new sorted list
def merge_two_list(first_sorted_list, second_sorted_list):
    i = j = 0
    # Create the result list, initialize as 0
    sorted_list = []
    # Use the while loop to consider all elements in both two lists
    while i < len(first_sorted_list) and j < len(second_sorted_list):
        # Track the smaller value of two list to append to the result list
        if first_sorted_list[i] <= second_sorted_list[j]:
            # Add value
            sorted_list.append(first_sorted_list[i])
            i+=1
        else:
            # Add value
            sorted_list.append(second_sorted_list[j])
            j+=1
    # Because there exist some cases that either I position is not approach length of first list
    while i < len(first_sorted_list):
        sorted_list.append(first_sorted_list[i])
        i+=1
    # Because there exist some cases that either J position is not approach length of second list
    while j < len(second_sorted_list):
        sorted_list.append(second_sorted_list[j])
        j+=1
    return sorted_list
# Definite the function that merge and sort the original list
def merge_sort(unordered_list):
    # Using while loop until the length of the list is less than 2
    while len(unordered_list) > 1:
        # Create a contemporary empty list
        tmp = []
        i = 0
        # Run from 0 to the length of the list - 1
        while i < len(unordered_list) - 1:
            # Append the merge of two list to the tmp list
            tmp.append(merge_two_list(unordered_list[i],unordered_list[i+1]))
            # Increment by two units
            i+=2
        # In case of length of list is odd, it must be added the last value to tmp list
        if i < len(unordered_list):
            tmp.append(unordered_list[i])
        # Assign the list for tmp list
        unordered_list = tmp
    return unordered_list[0]

# Input list
list_input = list(map(int, input().split()))
# Print initialize_chunks of the list
print(initialize_chunks(list_input))
# Two create two_element list, it has two cases
# If length of input list if even
if len(list_input) % 2 == 0:
    two_element_list = [[list_input[i], list_input[i + 1]] if list_input[i] < list_input[i+1] else [list_input[i+1], list_input[i]] for i in range(0,len(list_input),2)]
else:
# Otherwise
    two_element_list = [[list_input[i], list_input[i + 1]] if list_input[i] < list_input[i+1] else [list_input[i+1], list_input[i]] for i in range(0,len(list_input)-1,2)]
    two_element_list.append([list_input[len(list_input)-1]])
# Print the result
print(two_element_list)
# Print the last task
print(merge_sort(initialize_chunks(list_input)))


