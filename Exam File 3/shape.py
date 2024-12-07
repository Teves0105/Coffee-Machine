
def calculate_triangle(a: float, b: float, c:float):
    s = (a + b + c) / 2
    def area(a: float, b: float, c:float):
        return (s*(s-a)*(s-b)*(s-c))**(1/2)
    return s*2, area(a,b,c)

def calculate_rectangle(a: float, b: float):
    return 2*(a+b), a*b
def calculate_circle(r: float):
    pi = 3.14
    return 2*pi*r, pi*r*r
