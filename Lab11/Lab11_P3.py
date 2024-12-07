
# Define a class followed the requirement of the given assignment
class BankAccount:
    # Constructor
    def __init__(self, balance, interest_rate):
        self.balance = balance
        self.interest_rate = interest_rate
    # Define method to add by amount value
    def deposit(self, amount):
        self.balance += amount
    # Define method to withdraw by amount value
    def withdraw(self, amount):
        # If the current account less than amount value, return False
        if self.balance < amount:
            return False
        # Otherwise, implement subtraction
        self.balance -= amount
        return True
    # Define method to extract the current money
    def get_balance(self):
        return self.balance
    # Define method to apply an interest
    def apply_interest(self):
        self.balance *= self.interest_rate
        return self.balance
    # Print out when call the class
    def __str__(self):
        return f"Current balance: {self.balance:.1f}"

# Input in one line
initial_balance, interest_rate, deposit_amount, withdrawal_amount = input().split()

# Transform to the corrected type
initial_balance = int(initial_balance)
interest_rate = float(interest_rate)
deposit_amount = int(deposit_amount)
withdrawal_amount = int(withdrawal_amount)

# Assign to class
Current_BankAccount = BankAccount(initial_balance, interest_rate)

# Deposit period
Current_BankAccount.deposit(deposit_amount)
print(Current_BankAccount)
# Assign check variable to the withdraw method to check whether it is False or not
check = Current_BankAccount.withdraw(withdrawal_amount)
if not check:
    print(check)
else:
    print(Current_BankAccount)

# Apply the interest
Current_BankAccount.apply_interest()
print(Current_BankAccount)

