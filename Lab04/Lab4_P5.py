import math


def quadratic_solver(a, b, c):
    try:
        """
            Solve the quadratic equation
            Parameter: a (int), b (int), c (int)
            Result: the result of this function
        """


        # Transfer a, b, c value to the integer number
        a = int(a)
        b = int(b)
        c = int(c)

        # If a = 0, it's not a quadratic equation
        if a == 0:
            if b == 0:
                if c == 0:
                    # a = 0, b = 0, c = 0, infinite solutions
                    return("Infinite solutions")
                else:
                    # a = 0, b = 0, c != 0, no solutions
                    return("Error: No real solutions")
            else:
                # a = 0, but b != 0 => linear equation bx + c = 0
                x = -c / b
                return(f"Linear equation, solution: {x}")
        else:
            # a != 0, it's a quadratic equation
            delta = b ** 2 - 4 * a * c  # Calculate the discriminant
            if delta < 0:
                # No real solutions if delta is negative
                return("Error: No real solutions")
            elif delta == 0:
                # One real solution if delta is zero
                x = -b / (2 * a)
                return(f"Solutions: {x}")
            else:
                # Two real solutions if delta is positive
                x1 = (-b + math.sqrt(delta)) / (2 * a)
                x2 = (-b - math.sqrt(delta)) / (2 * a)
                return(f"Solutions: {x1}, {x2}")
    except ValueError:
        #If the input is invalid, this command line will implement
        return("Error: Invalid input.")

    finally:
        # Always print this, but if the function is linear equation, it's not printed
        if not (a==0 and b!=0):
            print("Attempted to solve the equation.")



# Input the value for a, b, c respectively
a = input()
b = input()
c = input()
# Implement the function to solve the problem
print(quadratic_solver(a, b, c))