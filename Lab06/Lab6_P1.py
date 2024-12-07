# Definite the function to implement five tasks
def list_operations(numbers):
    # Set the value for sum, max and min is equal to the first element of the list numbers
    sum = max = min = numbers[0]
    # Use the for loop to check all the element in list
    for i in range(1,len(numbers)):
        # Sum will compute the sum all the element in the list
        sum += numbers[i]
        # Variable max find the maximum value
        if max < numbers[i]:
            max = numbers[i]
        # Variable min find the minimum value
        if min > numbers[i]:
            min = numbers[i]
    # Use the method reverse() to reverse the list numbers
    numbers.reverse()

    # Print all the result
    print(sum)
    print(min)
    print(max)
    print(*numbers)

# Input the number of element and the list
n = int(input())
numbers = list(map(int, input().split()))

# Call the function
list_operations(numbers)