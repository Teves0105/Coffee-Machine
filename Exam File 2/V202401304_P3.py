def extract_unique_chars(s1, s2):
    # Check if both inputs are strings
    if not isinstance(s1, str) or not isinstance(s2, str):
        raise TypeError("Both inputs must be strings.")

    # Convert both strings to lowercase and filter out non-alphabetic characters
    s1_filtered = [char for char in s1.lower() if char.isalpha()]
    s2_filtered = [char for char in s2.lower() if char.isalpha()]

    # Initialize an empty list to store common characters
    common_chars = []

    # Iterate through the filtered characters of the first string
    for char in s1_filtered:
        # If the character is also in the second string and not already in common_chars, add it
        if char in s2_filtered and char not in common_chars:
            common_chars.append(char)

    # Sort the common characters alphabetically
    return sorted(common_chars)


# Example usage:
try:
    result = extract_unique_chars("Hello123!", "world!?")
    print(result)  # Output: ['l', 'o']
except TypeError as e:
    print(e)