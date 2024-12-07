

# Input three number num1, num2, num3 in one line respectively
num1, num2, num3 = map(int, input().split())

"""
This program whill sort three number from the lowest to the highest
I will check for three main condition below
"""
# if num1 is the lowest number
if num1 <= num2 and num1 <= num3:
    # if num2 <= num3 => num3 is the largest number
    if num2 <= num3:
        print(num1, num2, num3)
    # if num2 > num3 => num2 is the largest number
    else:
        print(num1, num3, num2)
# if num2 is the lowest number


elif num2 <= num1 and num2 <= num3:
    # if num1 <= num3 => num3 is the largest number
    if num1 <= num3:
        print(num2,num1,num3)
    # if not => num1 is the largest number
    else:
        print(num2,num3,num1)
# if num3 is the lowest number
else:
    # if num1 <= num2 => num2 is the largest number
    if num1 <= num2:
        print(num3,num1,num2)
    # if not => num1 is the largest number
    else:
        print(num3,num2,num1)





