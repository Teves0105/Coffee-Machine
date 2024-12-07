from operator import truediv

# Define Class Rectangle
class Rectangle:
    # Constructor
    def __init__(self,length,width):
        self.length = length
        self.width = width
    # Method to get area
    def area(self):
        return self.length*self.width
    # Method to get Perimeter
    def perimeter(self):
        return (self.length+self.width)*2

    # Print when call the class
    def __str__(self):
        return f"Rectangle(length={self.length}, width={self.width})"
    # Comparison two rectangle in terms of area
    def __eq__(self, another_rectangle):
        if self.area() == another_rectangle.area():
            return True
        else:
            return False

    def __lt__(self, another_rectangle):
        if self.area() < another_rectangle.area():
            return True
        else:
            return False


# Input
first_rectangle_length, first_rectangle_width = map(int,input().split())
second_rectangle_length, second_rectangle_width = map(int,input().split())

# Assign to two objects
First_rec = Rectangle(first_rectangle_length,first_rectangle_width)
Second_rec = Rectangle(second_rectangle_length,second_rectangle_width)


# Print the required results
print(First_rec)
print(Second_rec)
print(First_rec.area())
print(Second_rec.perimeter())

if First_rec.__eq__(Second_rec):
    print("equal")
elif First_rec.__lt__(Second_rec):
    print("smaller")
else:
    print("bigger")


