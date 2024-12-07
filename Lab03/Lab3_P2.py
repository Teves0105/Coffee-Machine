

def convert_temperature(tem: float, u: str) -> float:
    """
    Calculate area and perimeter of a rectangle

    Parameters
        tem (int): the given temperature
        u (int): the unit, either 'C' for Celsius or 'F' for Fahrenheit"
    """
    if u == 'C':
        # Convert from Celsius to Fahrenheit
        res = (tem * 9 / 5) + 32
    else:
        # Convert from Fahrenheit to Celsius
        res = (tem - 32) * 5 / 9
    return res

# input temperature and unit from keyboard
temperature = int(input())
unit = (input())
# calculate the result
result = convert_temperature(temperature, unit)
print(f"{result:.2f}")



