
# Define the class Employee as the baseclass
class Employee:
    # Constructor
    def __init__(self, name, employee_id):
        self.__name = name
        self.__employee_id = employee_id
    # Getter to get name
    def get_name(self):
        return self.__name
    # Getter to get the employee id
    def get_employee_id(self):
        return self.__employee_id
    # Define a method to calculate the salary
    def calculate_salary(self):
        return "NotImplementedError"

class FullTimeEmployee(Employee):
    # Constructor
    def __init__(self, name, employee_id, monthly_salary):
        super().__init__(name, employee_id)
        self.monthly_salary = monthly_salary
    # Define a method to calculate the salary
    def calculate_salary(self):
            return self.monthly_salary

class PartTimeEmployee(Employee):
    # Constructor
    def __init__(self, name, employee_id, hourly_rate, hours_worked):
        super().__init__(name, employee_id)
        self.hourly_rate = hourly_rate
        self.hours_worked = hours_worked

    # Define a method to calculate the salary
    def calculate_salary(self):
            return self.hourly_rate * self.hours_worked

# Input n lines
n =int(input())
for _ in range(n):
    one_line = list(input().split())
    # If length of the line equal to 3, it will be a full time employee
    if len(one_line) == 3:
        A_Staff = FullTimeEmployee(int(one_line[0]), one_line[1], int(one_line[2]))
        print(f"Employee ID: {A_Staff.get_name()}, Name: {A_Staff.get_employee_id()}, Salary: {A_Staff.calculate_salary():.1f}")
    # Otherwise, it will be a part-time employee
    elif len(one_line) == 4:
        A_Staff = PartTimeEmployee(int(one_line[0]), one_line[1], int(one_line[2]), int(one_line[3]))
        print(f"Employee ID: {A_Staff.get_name()}, Name: {A_Staff.get_employee_id()}, Salary: {A_Staff.calculate_salary():.1f}")


