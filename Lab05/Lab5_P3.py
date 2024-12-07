
# Input the two location, first one is the original location of the King and the latter is the new location of the King
l1 = input()
l2 = input()
# Extract the location l1 to the location in xy - intercept l1 => (x1,y1)
x1 = ord(l1[0]) - 96
y1 = int(l1[1])
# Extract the location l2 to the location in xy - intercept l2 => (x2,y2)
x2 = ord(l2[0]) - 96
y2 = int(l2[1])
# Let the variable Check == False, it will check for the location of the king whether it suitable or not
Check = False
# Calculate the suitable result
if abs(x1-x2) <= 1 and abs(y1-y2) <= 1:
    Check = True
# Print the result of Check
print(Check)