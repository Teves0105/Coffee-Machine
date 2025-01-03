def backtracking(array, k, visited):
    if k == len(array):
        print("".join(array))  # Print the current permutation
    else:
        for i in range(len(characters)):
            if not visited[i] and not characters[i] == array[k-1]:  # Check if the character is not yet used
                array[k] = characters[i]
                visited[i] = True  # Mark the character as used
                backtracking(array, k + 1, visited)
                visited[i] = False  # Backtrack: unmark the character

# Input data
characters = ['A', 'A', 'B', 'E', 'B']
array = [''] * len(characters)  # Array to store the current permutation
visited = [False] * len(characters)  # Track which characters are used

# Start backtracking
backtracking(array, 0, visited)
