def cumulative_product(numbers):
    if not all(numbers[i].isdigit() for i in range(len(numbers))):
        raise ValueError("All elements must be integer")
    if numbers == []:
        raise ValueError("List is empty")
    new_numbers = [int(element) for element in numbers if int(element)%2==0]
    for i in range(1,len(new_numbers)):
        new_numbers[i] *= new_numbers[i-1]
    if new_numbers == []:
        return([0])
    else:
        return(new_numbers)


try:
    numbers = list(map(str,input().split()))
    print(cumulative_product(numbers))
except ValueError as e:
    print(e)