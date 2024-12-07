
# Create a function that find the minimum value and maximum value
def find_min_max(unsorted_list):
    min_value = unsorted_list[0]
    max_value = unsorted_list[0]
    for number in unsorted_list:
        if min_value > number:
            min_value = number
        if max_value < number:
            max_value = number
    return min_value, max_value
# Define a function that will return a list with counting frequency of each number
def count_frequency(unsorted_list,min_value, max_value):
    # Create the list include 0 times from minimum value to maximum value
    counting_list = [0]*(max_value - min_value + 1)
    # Consider number from min to max value
    for number in range(min_value,max_value+1):
        # each element i th will have the counting of its occurrence
        counting_list[number-min_value] = unsorted_list.count(number)
    return counting_list
# Define a function that sorting the given unsorted list
def counting_sort(unsorted_list):
    min_value, max_value = find_min_max(unsorted_list)
    frequency_list = count_frequency(unsorted_list,min_value,max_value)
    # Create an empty result list
    result_list = []
    # Consider all element in frequency list
    for i in range(len(frequency_list)):
        # Decrement each element to 0
        while frequency_list[i] != 0:
            # Append each number to the result list
            result_list.append(i+min_value)
            frequency_list[i] -=1
    return result_list
# Input
unsorted_list = list(map(int, input().split()))
tuple_of_min_max_value = find_min_max(unsorted_list)

# Print the answer
print(tuple_of_min_max_value[0], tuple_of_min_max_value[1])
print(count_frequency(unsorted_list, tuple_of_min_max_value[0], tuple_of_min_max_value[1]))
print(counting_sort(unsorted_list))

