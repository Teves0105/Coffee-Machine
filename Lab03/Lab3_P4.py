import math_operation


"""
input two number for the first number and the second number, and an operator
   fi: the first number
   se: the second number
   op: operator include +, -, *, /, **, //
"""
fi, se = map( int, input().split() )
op = input()

if op == '+':
    print( f"{math_operation.add(fi, se):.2f}" )
elif op == '-':
    print( f"{math_operation.subtract(fi, se):.2f}" )
elif op == '*':
    print( f"{math_operation.multiply(fi, se):.2f}" )
elif op == '/':
    print( f"{math_operation.divide(fi, se):.2f}" )
elif op == '**':
    print( f"{math_operation.power(fi, se):.2f}" )
else:
    print( f"{math_operation.integer_divide(fi, se):.2f}" )


