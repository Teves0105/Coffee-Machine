# Your code for the problem
import time

def permute(nums):
    # Create a new function, this will use the recursive method to solve
    def backtrack(start):
        # Base case: if start is at the end of the list, return the list itself
        if start == len(nums):
            result.append(nums[:])  # Append a copy of the current permutation
            return

        # Recursive case: try every possible position for each number
        for i in range(start, len(nums)):
            # Swap the current index with the start index
            nums[start], nums[i] = nums[i], nums[start]
            # Recursively generate the permutations for the next position
            backtrack(start + 1)

            # Backtrack (restore the original configuration)
            nums[start], nums[i] = nums[i], nums[start]

    # The result will store all the permutations
    result = []

    # Start the recursion from the first index (0)
    backtrack(0)

    return result
nums = list(map(int, input().split()))
nums.sort()
# Sort the input list to ensure the permutations are generated in sorted order
permutations = permute(nums)
# Sort the list in list permutations to adapt the requirement of the assignment
permutations.sort()
for one_list in permutations:
    for number in one_list:
        print(number, end=' ')
    print()


# Comment the execution time results
"""
Input: 2 3 5
Recursive: 
2 3 5
2 5 3
3 2 5
3 5 2
5 2 3
5 3 2
Execution Time (Sequential): 0.00009440 seconds

Input: 38 68
Recursive:
38 68
68 38
Execution Time (Sequential): 0.00005460 seconds
"""