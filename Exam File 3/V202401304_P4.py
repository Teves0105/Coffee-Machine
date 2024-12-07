



drinks_list = [
    "Green tea",
    "Black tea",
    "Oolong tea",
    "White tea",
    "Lemonade",
    "Herbal tea",
    "Milk tea",
    "Bubble milk tea"
]

print("What do you want to do?")
print("1. Print the drink list")
print("2. Find drink by keyword")
print("3. Add a new drink to list")
print("4. Delete a drink")
print("Please select a number (from 1->4): ")
choice = int(input())

if choice == 1:
    print(f"There are {len(drinks_list)} drinks in the list:")
    print(drinks_list)
elif choice == 2:
    keyword = input("Input a keyword")
    new_keyword = keyword.lower()
    new_list = [element.lower() for element in drinks_list]
    count = 0
    arr_count =[]
    for i in range(len(new_list)):
        if new_keyword in new_list[i]:
            arr_count.append(drinks_list[i])
            count+=1
    if count > 0:
        print(f"There are {count} drinks including '{keyword}': {arr_count}")
    else:
        print(f"No drink including the keyword '{keyword}'")
elif choice == 3:
    keyword = input("Input a keyword")
    new_keyword = keyword.lower()
    new_list = [element.lower() for element in drinks_list]
    if new_keyword in new_list:
        print("This drink is already in the list")
    else:
        new_keyword = new_keyword[:len(new_keyword)-3].title() + "tea"
        drinks_list.append(new_keyword)
        print(f"There are {len(drinks_list)} drinks in the list:")
        print(drinks_list)
elif choice == 4:
    keyword = input("Input the name of the drink you want to delete:")
    new_keyword = keyword.lower()
    new_list = [element.lower() for element in drinks_list]
    if new_keyword in new_list:
        drinks_list.pop(new_list.index(new_keyword))
        print(f"The drink {keyword} is successfully deleted from the list")
        print(f"There are {len(drinks_list)} drinks in the list:")
        print(drinks_list)
    else:
        print(f"The drink '{keyword}' is not in the list, please try again.")
else:
    print("Please input an integer between 1 and 4")