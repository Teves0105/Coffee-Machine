import shape


in_shape = input()

if in_shape == "Triangle":
    a,b,c = map(int, input().split())
    perimeter, area = shape.calculate_triangle(a, b, c)
    print(f"{perimeter:.2f} {area:.2f}")
elif in_shape == "Rectangle":
    a, b = map(int, input().split())
    perimeter, area = shape.calculate_rectangle(a, b)
    print(f"{perimeter:.2f} {area:.2f}")
else:
    r = int(input())
    perimeter, area = shape.calculate_circle(r)
    print(f"{perimeter:.2f} {area:.2f}")

