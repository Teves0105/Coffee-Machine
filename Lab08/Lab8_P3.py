# Create an empty dictionary cart
cart = {

}
# Input ont_line for each line
one_line = input()
# This while-loop will execute until it equal to string of "quit"
while one_line != "quit":
    # Split each word in this line
    new_list = one_line.split()



    # If the first element equal to remove, it means that discard the second element in the dictionary
    if new_list[0] == "remove":
        # If this element exist in cart, it will be removed
        if new_list[1] in cart:
            # Before removing, print it to the screen
            print(f"{new_list[1]}: {cart[new_list[1]]}")
            # Remove through pop function
            cart.pop(new_list[1])
        else:
            # But if it is not exist in cart, it will print the comment line
            print("Item not found")
    # If the first element equal to add, it means that adding an element to cart
    elif new_list[0] == "add":
        # If this element exist before, it will increase by plus the original value and present value
        if new_list[1] in cart:
            cart[new_list[1]] =str(int(cart[new_list[1]]) + int(new_list[2]))
        else:
        # Otherwise, assign a new key,value for dictionary
            cart[new_list[1]] = new_list[2]
        # Print the comment to the screen
        print(f"{new_list[1]}: { cart[new_list[1]]}")
    # If the first element equal to show, it means that show the cart to the screen
    elif new_list[0] == "show":
        # But if cart is empty, it will print the line "Cart is empty" to the screen
        if cart == {}:
            print("Cart is empty")
        else:
            # Using variable count to print the suitable icon ","
            count = 0
            for key, value in sorted(cart.items()):
                print(f"{key}: {value}",end='')
                count+=1
                if count != len(cart):
                    print(', ',end='')
            print()
    # Read again
    one_line = input()
