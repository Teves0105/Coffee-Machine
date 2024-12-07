"""
    Create a function name count_vowels that take the string as an input and
    then it weill return the number of character in the element of ['u','e','o','a','i']
"""
def count_vowels(text: str) -> int:
    # Counting the vowels
    count = text.count('u') + text.count('e') + text.count('o') + text.count('a') + text.count('i')
    return count
# Input the string name text
text = input()

# Lower case all the characters and then print the result
print(count_vowels(text.lower()))