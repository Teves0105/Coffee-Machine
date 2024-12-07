def analyze_words(words):
    result = []

    for index, word in enumerate(words):
        # Create a list to count the frequency of each character
        new_set = list(set(word))
        new_set.sort()
        char_count = [word.count(char) for char in new_set]
        # Sort the characters alphabetically and format the output
        formatted_counts = ", ".join(f"{new_set[i]}: {char_count[i]}" for i in range(len(new_set)))
        # Construct the final string for this word
        result.append(f"{index} - {formatted_counts}")


    return result

n = int(input())  # Read number of words
words = input().split()  # Read the words
output = analyze_words(words)  # Analyze the words
for line in output:
    print(line)  # Print each formatted line