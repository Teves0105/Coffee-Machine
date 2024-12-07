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


def print_list(drinks_list):

    print(f"There are {len(drinks_list)} drinks in the list:\n{drinks_list}")


def find_drink_by_keyword(drinks_list):

    input2 = input('Input a keyword: ')

    keyword = input2.lower()  # Get keyword input

    list_found_drink = list(filter(lambda drink: keyword in drink.lower(), drinks_list))

    if list_found_drink:

        print(f"There are {len(list_found_drink)} drinks including '{input2}': {list_found_drink}")

    else:

        print(f'No drink including the keyword "{input2}".')


def add_to_list(drinks_list):

    input3 = input('Input a new drink: ')

    new_drink = input3.capitalize()

    if new_drink in drinks_list:

        print("This drink is already in the list.")

    else:

        drinks_list.append(new_drink)

        print_list(drinks_list)


def delete_drink(drinks_list):

    input4 = input('Input the name of the drink you want to delete: ')

    drink = input4.capitalize()

    if drink not in drinks_list:

        print(f'The drink "{input4}" is not in the list, please try again.')

    else:

        drinks_list.remove(drink)

        print(f'The drink "{input4}" is successfully deleted from the list.')

        print_list(drinks_list)


try:

    user_input = int(input("""What do you want to do?

1. Print the drink list

2. Find drink by keyword

3. Add a new drink to the list

4. Delete a drink

Please select a number (from 1 to 4): """))

except ValueError:

    print('Please input an integer.')

else:

    if user_input == 1:

        print_list(drinks_list)

    elif user_input == 2:

        find_drink_by_keyword(drinks_list)

    elif user_input == 3:

        add_to_list(drinks_list)

    elif user_input == 4:

        delete_drink(drinks_list)

    else:

        print('Please input an integer between 1 and 4.')