

def calculate_distance(xa: float, ya: float, xb: float, yb: float) -> float:

    def square_difference(xa: float, ya: float, xb: float, yb: float):
        # get the square of location between two points
        square_res = (xa - xb)**2 + (ya - yb)**2
        return square_res
    # get the difference distance of two points
    return square_difference(xa,ya,xb,yb)**0.5


"""
input the number for the location of two point A and B
    A have the location of xa, ya
    B have the location of xb, yb
"""

xa,ya = map(float, input().split())
xb,yb = map(float, input().split())

print(f"{calculate_distance(xa,ya,xb,yb):.2f}")

