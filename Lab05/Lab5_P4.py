
# Input the string to converted period
string = input()

"""
if in string exist any word "secret", it will replace to "XXXXXX"
if in string exist a list of character "a", "e", "i", "o", "u" => it will replace it to "@", "3", "!", "0", "v"
"""
string = string.replace("secret","XXXXXX")
string = string.replace("a","@")
string = string.replace("e","3")
string = string.replace("i","!")
string = string.replace("o","0")
string = string.replace("u","v")

# Check the length of the string, if the length is even number, it will return the upper string, otherwise return the lower string
if len(string)%2 == 0:
    string = string.upper()
else:
    string = string.lower()
# Print the finally result
print(string)

