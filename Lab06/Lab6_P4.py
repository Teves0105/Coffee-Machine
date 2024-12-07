# Definite the function to find the satisfied list
def filter_by_length(words, min_length):
    """
    Create the new list and using list comprehension to complete the list
    element_words is the element in the words
    if the condition satisfied, it will add to the list new_words
    """
    new_words = [element_words for element_words in words if len(element_words) >= min_length]
    return new_words

# Input the number of element in the list, input the list words and the min_length respectively
n = int(input())
words = list(map(str, input().split()))
min_length = int(input())

# Print the list without packing the list by using *
print(*filter_by_length(words, min_length))
