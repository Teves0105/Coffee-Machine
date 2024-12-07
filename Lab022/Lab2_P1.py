#input two integer in one line through the way of split
inp_str = input()
a,b= inp_str.split()

#Transfer from the string to integer values
a = int(a)
b = int(b)

#Calculate the sum
sum = a + b

#Calculate the difference
diff = a - b

#Calculate the multiplication
times = a*b

#Calculate the division
div = a//b

print(sum, diff, times, div)
