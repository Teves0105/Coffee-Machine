# Input the number n
n = int(input())
# Create a dictionary to extract how many anagram groups
dict = {}
# Consider all elements in the given number
for _ in range(n):
    # Input the word to check
    word = input()
    # Convert to the tuple of the list
    temp_tuple = tuple(sorted(list(word)))
    # Assign the key temp_tuple and the value 1 for dictionary
    dict[temp_tuple] = 1
# Print the length of the dictionary
print(len(dict))
