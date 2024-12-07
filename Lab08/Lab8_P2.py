# Input the number of employees
n = int(input())
# Create a new dictionary to tackle this assignment
new_dict = {}

for i in range(n):
    # Read one_line from the input split by space
    one_line = tuple(input().split())
    # Assign 8 variable name and the number of seven hours
    name,hours1,hours2,hours3,hours4,hours5,hours6,hours7 = one_line
    # Create an empty hour_day list to append all hours to list
    hour_day = (int(hours1),int(hours2),int(hours3),int(hours4),int(hours5),int(hours6),int(hours7))
    # Assign to the new_dict, the key is string, the value is a list
    new_dict[name] = hour_day
# Create the new dictionary to solve the next requirement
satisfied_dict = {}
for key,value in new_dict.items():
    new_dict[key] = sum(value)
    # If the value > 40 hours, the satisfied_dict will be assigned
    if new_dict[key] > 40:
        satisfied_dict[key] = new_dict[key]

# Sorted_dict as a new list
sorted_dict = (sorted(satisfied_dict.items(), key=lambda x: (-x[1], x[0])))

# Print it to the screen
print(sorted_dict)