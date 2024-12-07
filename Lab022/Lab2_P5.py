# Read the input boolean values
# the a, b, c will get the boolean value through the comparison with the string 'True'
a = input() == 'True'
b = input() == 'True'
c = input() == 'True'

# Calculate the required expressions
expr1 = not a
expr2 = a and b
expr3 = a or b
expr4 = a and (b or c)

# Output the results, separated by spaces
print(expr1, expr2, expr3, expr4)