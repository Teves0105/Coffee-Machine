# Define the class Polynomial
class Polynomial:
    # Constructor
    def __init__(self, coefficients):
        self.coefficients = coefficients
        while self.coefficients and self.coefficients[-1] == 0:
            self.coefficients.pop()
    # Define the "+" method to add two objects
    def __add__(self, other):
        # Find the max degree between two polynomials
        max_length = max(len(self.coefficients), len(other.coefficients))
        # two lines below to make the adding period become more easily
        self.coefficients = self.coefficients + [0]*(max_length - len(self.coefficients))
        other.coefficients = other.coefficients + [0]*(max_length - len(other.coefficients))

        # Adding period
        i = 0
        # Create the result polynomial
        added_coefficients = []
        while i < max_length:
            added_coefficients.append(self.coefficients[i] + other.coefficients[i])
            i+=1
        # Convert to the object and return
        return Polynomial(added_coefficients)

    # Define the "*" method to add two objects
    def __mul__(self, other):
        # Find the max degree between two polynomials
        max_length = len(self.coefficients) + len(other.coefficients) - 1
        # Set the value for the created list to implement the multiplied process
        multiplied_list = [0]*max_length
        for i in range(self.degree() + 1):
            for j in range(other.degree() + 1):
                # Adding with the same degree after multiply
                multiplied_list[i+j] += self.coefficients[i] * other.coefficients[j]
        # Return the object after convert
        return Polynomial(multiplied_list)

    # Define the method to find out the degree of a polynomial
    def degree(self):
       return len(self.coefficients) - 1

    # Print to the screen
    def __str__(self):
        # If the polynomial is an empty list, it will return 0
        if not self.coefficients:
            return "0"
        # Create a list, which will represent the given polynomial
        list_of_equation = []
        for i in range(len(self.coefficients)):
            # If the coefficient different from 0, it will follow this line
            if self.coefficients[i]:
                # If the exponent equal to 0, the variable x will not print because x^0 = 1
                if i == 0:
                    list_of_equation.append(f"{self.coefficients[0]}")
                # Else if the exponent equal to 1, the variable x will print x instead of x^1
                elif i == 1:
                    # If the coefficient equal to 1, it will not print
                    if self.coefficients[i] == 1:
                        list_of_equation.append(f"x")
                    # If the coefficient equal to -1, it will just print '-' symbol
                    elif self.coefficients[i] == -1:
                        list_of_equation.append(f"-x")
                    # Else, print the coefficient
                    else:
                        list_of_equation.append(f"{self.coefficients[1]}x")
                # Otherwise, the exponent equal to any value except for 0, 1
                else:
                    # If the coefficient equal to 1, it will not print
                    if self.coefficients[i] == 1:
                        list_of_equation.append(f"x^{i}")
                    # If the coefficient equal to -1, it will just print '-' symbol
                    elif self.coefficients[i] == -1:
                        list_of_equation.append(f"-x^{i}")
                    # Else, print the coefficient
                    else:
                        list_of_equation.append(f"{self.coefficients[i]}x^{i}")
        # Declare the result string to return the resulting of this assignment
        result = " + ".join(list_of_equation).replace("+ -","- ")
        # Tackle for the special case
        if result[0] == '-':
            result = '- ' + result[1:]
        return result


# Read inputs
equation_first = list(map(int, input().split()))
equation_second = list(map(int, input().split()))

# Create Polynomial objects
poly1 = Polynomial(equation_first)
poly2 = Polynomial(equation_second)

# Calculate sum and product
poly_sum = poly1 + poly2
poly_product = poly1 * poly2

# Output results
print("Sum:", poly_sum)
print("Product:", poly_product)



