# Create a function to return the final dictionary
def count_word_frequencies(text):
    # Assign to a new string which have all lowercase character
    new_text = text.lower()
    # Convert this string to a new list split by spacing
    for word in list(new_text.split()):
        # if each word exist in the dict, it will increment
        if word in result_dict:
            result_dict[word] += 1
        else:
        # Otherwise, it will assign for dict
            result_dict[word] = 1
    # Sorted again the dict and assign to the final dict
    even_result_dict = dict(sorted(result_dict.items()))
    return(even_result_dict)
# Create a dictionary
result_dict = {}
# Input the text
text = input()
# This variable "count" use to print the suitable icon ','
count = 0
even_result_dict = count_word_frequencies(text)
# Print the length of the dictionary
print(len(even_result_dict))
# Consider key and value in the even_result_dict
for key,value in even_result_dict.items():
    # The form of print to the screen
    print(f"{key}:  {value}",end='')
    # If count is less than len of dict - 1, it will print the icon ','
    if count != len(even_result_dict) - 1:
        print(',',end=' ')
    # Increment count
    count+=1