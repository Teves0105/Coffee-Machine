# the file contains a lot of function which implement the function of add, subtract, multiply, divide, power, and integer divide of two numbers

def add(first: int, second: int) -> float:
    # calculate the total of first and second number
    return first + second

def subtract(first: int, second: int) -> float:
    # calculate the subtract of first and second number
    return first - second

def multiply(first: int, second: int) -> float:
    # calculate the  of multiple of first and second number
    return first * second

def divide(first: int, second: int) -> float:
    # calculate the divide of first and second number
    if second == 0:
        raise ValueError("Cannot divide by zero")
    return first / second

def power(first: int, second: int) -> float:
    # calculate the power of first and second number
    return first ** second

def integer_divide(first: int, second: int) -> float:
    # calculate the divide and get the integer number of first and second number
    if second == 0:
        raise ValueError("Cannot divide by zero")
    return first // second