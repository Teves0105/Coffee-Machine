# Input n rows
n = int(input())

# Implement to draw the hollow pyramid
for i in range(n):
    # This for-loop will print the blank characters
    for j in range(n-i-1):
        print(end= ' ')
    # This for-loop will print the star icon *
    for j in range(2*(i+1) - 1):
        print("*",end='')
    # After completed print in each row, this command will write down the line
    print()