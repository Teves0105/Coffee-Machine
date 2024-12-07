# Input the year which needed to be checked whether it is a leap year or not
year = int(input())

# Let a variable Check = False
Check = False
"""
Using condition to check for the given year 
if year % 4 == 0 and year % 100 == 0 and year % 400 == 0 => Check becomes true
But if year % 400 != 0 => Check becomes False
But if year % 100 != 0 => Check becomes True
"""
if year%4==0:
    if year%100==0:
        if year%400==0:
            Check = True
        else:
            Check = False
    else:
        Check = True
# Print the result of Check
print(Check)

