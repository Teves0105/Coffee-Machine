


def triangle_properties(leng: int, wid: int) -> tuple[int, int]:
    """
    Calculate area and perimeter of a rectangle

    Parameters
        leng (int): the length of a rectangle
        wid (int): the width of a rectangle

    returns
        Tuple[int, int]: Two values demonstrating area and perimeter of the rectangle

    """
    pe = 2 * ( leng + wid )

    are = leng * wid

    return are, pe

# input from keyboard
length, width = map(int, input().split())

# calculate area, perimeter
area, perimeter =triangle_properties(length,width)

# print the area and perimeter of the rectangle
print(area, perimeter)


