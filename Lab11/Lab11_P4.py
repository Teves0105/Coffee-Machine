

class Fraction:
    # Constructor
    def __init__(self, numerator, denominator):
        self.__numerator = numerator
        self.__denominator = denominator

    # Display the fraction
    def display(self):
        return f"{self.__numerator}/{self.__denominator}"

    # Add two fraction
    def add(self, other):
        new_numerator = self.__numerator * other.__denominator + self.__denominator * other.__numerator
        new_denominator = self.__denominator * other.__denominator

        added_fraction = Fraction(new_numerator,new_denominator)

        return added_fraction

    # Product of two fractions
    def multiply(self, other):
        new_numerator = self.__numerator * other.__numerator
        new_denominator = self.__denominator * other.__denominator
        multiplied_fraction = Fraction(new_numerator, new_denominator)

        return multiplied_fraction
    # Compute the gcd of two number a and b
    def gcd(self, a, b):
        while b:
            a, b = b, a%b
        return a
    # Simplify the given fraction
    def simplify(self):
        gcd_of_fraction = self.gcd(self.__numerator,self.__denominator)
        new_numerator = self.__numerator//gcd_of_fraction
        new_denominator = self.__denominator//gcd_of_fraction

        simplified_fraction = Fraction(new_numerator, new_denominator)

        return simplified_fraction

# Input two fraction through two lines
first_fraction = list(map(int, input().split()))
second_fraction = list(map(int, input().split()))

# Assign to two objects of class
First_frac = Fraction(first_fraction[0], first_fraction[1])
Second_frac = Fraction(second_fraction[0], second_fraction[1])

# Print the results
print((First_frac.add(Second_frac)).simplify().display())
print((First_frac.multiply(Second_frac)).simplify().display())