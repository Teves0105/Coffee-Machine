def expression(a: float, b = 25.8):
    try:
        assert a >= 0 and b >= 0, "Only non-negative numbers must be provided."
        return (2+a)/b
    except ZeroDivisionError:
        return -1
    except AssertionError as e:
        return e
x, y = map(float, input().split())
result = expression(x, y)
if isinstance(result, (int,float)):
    print(f"{result:.2f}")
else:
    print(result)
