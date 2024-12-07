# definite the function to return the median value of the List
def find_median(numbers) -> float:
    # Sort the list to find the median value easily
    numbers.sort()
    # If the number of list n is odd number, the median value is located in the middle of the sorted list
    if n%2 == 1:
        return numbers[n//2]
    # Otherwise, two element which is located in the middle of the sorted list, the result is the average of this two values
    else:
        return (numbers[n//2-1] + numbers[n//2]) /2

# Input the number of element and the list
n = int(input())
numbers = list(map(int, input().split()))

# Print the result
print(f"{find_median(numbers):.1f}")




