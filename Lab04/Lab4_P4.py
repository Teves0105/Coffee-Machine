"""
    Create division function that take the equation of a over b
    But if any issues like either a and b is negative number
            and b equal to 0
        It will print out some problem
"""
def division(a, b):
    # Try to get the division
    try:
        a = int(a)
        b = int(b)
        result = a / b
    # If b == 0, this command line will run
    except ZeroDivisionError:
        print("Error: Division by zero is not allowed.")
    # If each of given number a and b is negative number, this command line will run
    except ValueError:
        print("Error: Invalid input.")
    # If a and b are valid, this command line will run
    else :
        print(f"Result: {result}")
    # Always implement
    finally:
        print("Execution complete.")
# Input two integer numbers a and b respectively
a = input()
b = input()
# Run the function
division(a,b)