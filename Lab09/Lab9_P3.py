

# Input first_string and second_string
first_string = input()
second_string = input()
# Create a new dictionary to track the index of each character in the second_string to make the comparison easily
count_dict = {character: index for index, character in enumerate(second_string)}
# Convert from string to the list of character of string
first_string = list(first_string)
# Check all the character in the first string
for i in range(len(first_string)):
    # Using the selection sort to sorted follow to the count_dict rule
    min_index = i
    for j in range(i+1, len(first_string)):
        if count_dict[first_string[j]] < count_dict[first_string[min_index]]:
            min_index = j
    # Transform two value in index i and min_index
    first_string[i], first_string[min_index] = first_string[min_index], first_string[i]

print(''.join(list(first_string)))


