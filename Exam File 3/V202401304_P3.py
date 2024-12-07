


s = input()
c = int(input())

first_new_s = s[::-1]
second_new_s = ''.join([chr((ord(character) - 97 + c)%26+ 97) for character in list(first_new_s)])
if first_new_s.find("woman") != -1 and second_new_s.find("woman") != -1:
    if first_new_s.find("woman") < second_new_s.find("woman"):
        new_list = list(second_new_s[:first_new_s.find("woman")+5])
    else:
        new_list = list(second_new_s[:second_new_s.find("woman") + 5])
elif first_new_s.find("woman") != -1:
    new_list = list(second_new_s[:first_new_s.find("woman")+5])
elif second_new_s.find("woman") != -1:
    new_list = list(second_new_s[:second_new_s.find("woman") + 5])
else:
    new_list = list(second_new_s)
print(''.join(new_list))

