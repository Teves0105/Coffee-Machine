# Global dictionary for memoization
memo = {}


def fibonacci(n):
    # Error handling: Check if n is an integer and non-negative
    if not isinstance(n, int):
        raise ValueError("Input must be an integer.")
    if n < 0:
        raise ValueError("Input must be a non-negative integer.")

    # Base cases
    if n == 0:
        return 0
    elif n == 1:
        return 1

    # Check if the result is already cached
    if n in memo:
        return memo[n]

    # Recursive call with memoization
    result = fibonacci(n - 1) + fibonacci(n - 2)

    # Cache the result
    memo[n] = result

    return result


# Example usage:
try:
    result = fibonacci(5.0)
    print(f"The 10th Fibonacci number is: {result}")
except ValueError as e:
    print(e)