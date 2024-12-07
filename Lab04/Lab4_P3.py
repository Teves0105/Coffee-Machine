# Create the function calculate_area to compute the area based on the given length and width
def calculate_area(length: int, width: int) -> int:
    # If length is positive number, it will run normally. Otherwise, the appropriate error message will be printed
    assert (length > 0), "Length must be positive."

    # If width is positive number, it will run normally. Otherwise, the appropriate error message will be printed
    assert (width > 0), "Width must be positive."

    # Return the area
    return length * width
# Input the length and the width of the rectangle, respectively
length = int(input())
width = int(input())

# Calculate the area of a rectangle and assigned it for A
A = calculate_area(length,width)

# Print the result
print(f"Area: {A}")