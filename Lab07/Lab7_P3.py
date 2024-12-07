# Enter the steps of the path can be either U or D.
string = input()
"""
Set two variables to 0, count is the result of the problem
res_run is variable which will check to see where the current state is
above sea, surface, or underwater.
"""
count = 0
res_run = 0
i = 0

# Implement the while-loop
while i < len(string):
    # If the character == 'D' (Down) the res_run will decrease 1 unit
    if string[i] == 'D':
        res_run -= 1
    # Otherwise, the res_run will increase 1 unit
    else:
        res_run += 1
    """
    If res_run == 0, it means the person step back to the sea level
    But there are two cases to step back, one from Up to Down and 
    another one is from Down to Up
    the correct to step back is from Down to Up
    So that, the condition string[i]=='U" must be added
    """
    if res_run == 0 and string[i] == 'U':
        count+=1
    # Increment
    i+=1

# Print the result
print(count)