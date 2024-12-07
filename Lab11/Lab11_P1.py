

class Car:
    def __init__(self, speed, consumption_rate, fuel_level):
        # Code here for initiate speed in kim/ h
        self.speed = speed
        # Code here for initiate fuel consumed per hour
        self.consumption_rate = consumption_rate
        # Code here for initiate fuel level
        self.fuel_level = fuel_level

    def can_reach(self, distance):
        """
        Check if the car can reach the given distance based on
          current fuel level.
        :param distance: Distance to the destination in kilometers
        :return: True if it can reach, False otherwise
        """
    
        # Code here
        if self.fuel_level/self.consumption_rate*self.speed >= distance:
            return True
        else:
            return False

    def refuel_cost(self, price_per_unit):
        """
        Calculate the cost to refuel the car back to 100 fuel
            levels .

        :param price_per_unit: Cost of one unit of fuel
        :return: Cost to refuel to 100 fuel levels
        """

        # Code here
        return ((100-self.fuel_level)*price_per_unit)

# Input five elements
speed, consumption_rate, current_fuel_level, distance, price = map(int,input().split())

A_Car = Car(speed, consumption_rate, current_fuel_level)
# Print three required answers
print(A_Car.speed, A_Car.consumption_rate, A_Car.fuel_level)

print(A_Car.can_reach(distance))

print(A_Car.refuel_cost(price))