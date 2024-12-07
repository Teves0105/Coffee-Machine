# Create the function is_palindrome to check whether the string text is a palindrome string or not
def is_palindrome(text: str) -> bool:
    """
    text is the original string
    text[::-1] is the reverse of the original string
    :return:
    if the text is the palindrome then return True, otherwise return False
    """
    if text == text[::-1]:
        return True
    else:
        return False
# Input the text
text = input()

# Check palindrome text
if is_palindrome(text):
    print("True")
else:
    print("False")