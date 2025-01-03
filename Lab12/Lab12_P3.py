

# Define class Vehicle as a base class
class Vehicle:
    # Constructor
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    # Define the display_info to display to the screen
    def display_info(self):
        print(f"Brand: {self.brand}, Model: {self.model}, Year: {self.year}, ",end='')

# Define a subclass named Car which inherits from Vehicle
class Car(Vehicle):
    # Constructor
    def __init__(self, brand, model, year, num_doors):
        # Use super() to call to the base class to implement
        super().__init__(brand, model, year)
        self.num_doors = num_doors

    # Display_infor definition to display to the screen
    def display_info(self):
        # Call to the baseclass method
        super().display_info()
        # Print to the screen
        print(f"Number of doors: {self.num_doors}")

# Define a subclass named Truck which inherits from Vehicle
class Truck(Vehicle):
    #Constructor
    def __init__(self,brand, model, year, payload_capacity):
        # Use super() to call to the base class to implement
        super().__init__(brand, model, year)
        self.payload_capacity = payload_capacity

    def display_info(self):
        # Call to the baseclass method
        super().display_info()
        # Print to the screen
        print(f"Payload Capacity: {self.payload_capacity}")

# Input n lines
n = int(input())
# Executing process
for _ in range(n):
    one_line = input().split()
    if one_line[0] == 'Car':
        off_brand = one_line[1]
        off_model = one_line[2]
        off_year = one_line[3]
        off_num_doors = one_line[4]
        Car(off_brand,off_model,off_year,off_num_doors).display_info()
    else:
        off_brand = one_line[1]
        off_model = one_line[2]
        off_year = one_line[3]
        off_payload_capacity = one_line[4]
        Truck(off_brand,off_model,off_year,off_payload_capacity).display_info()
