#Enter the math expressions
inp_str = input()
a,c,b= inp_str.split()

#Transfer the value a and b from string to integer
a = int(a)
b = int(b)

#check the operation for character c, whether it is +, -, *, or /
if (c=='+'): print(a+b)
elif (c=='-'): print(a-b)
elif (c=='*'): print(a*b)
else: print(a//b)
