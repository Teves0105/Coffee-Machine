

# Define class Account
class Account:
    # Constructor with two parameter id and balance
    def __init__(self, account_id, balance):
        self._account_id = account_id
        self.__balance = balance

    # Define the function of depositing by amount
    def deposit(self, amount):
        self.__balance += amount

    # Define the function of withdrawing by amount
    def withdraw(self, amount):
        if self.get_balance() >= amount:
            self.__balance -= amount

    # Getter to get the value of private attribute of balance
    def get_balance(self):
        return self.__balance

    # Setter the new value for private attribute
    def set_balance(self,new_balance):
        self.__balance = new_balance

    # Getter for the account_id (protected class)
    def get_account_id(self):
        return self._account_id


# Define class CheckingAccount which inherits Account class
class CheckingAccount(Account):
    # Constructor with three parameter including the baseclass parameter and fee
    def __init__(self, account_id, balance, fee = 5):
        super().__init__(account_id, balance)
        self.__fee = fee

    # Overriding method withdraw
    def withdraw(self, amount):
        # If amount less than 0, it will print the report
        if amount < 0:
            print("Invalid withdrawal amount.")
        # Furthermore, if the process of withdraw cannot implement, the screen also print another report
        elif self.get_balance() < amount + self.__fee:
            print("Insufficient balance.")
        # Otherwise, if the process is implemented successfully, the value of balance will be assigned to the new value
        else:
            # Set the value for balance after withdrawing
            self.set_balance(self.get_balance() - amount - self.get_fee())
            # Print to the screen
            print(f"Withdrawal successful from account {self._account_id} (including fee of {self.__fee}). Updated balance: {self.get_balance()}")
    # Overriding method deposit
    def deposit(self, amount):
        # Set the new value for balance after depositing
        self.set_balance(self.get_balance() + amount)
        # Print to the screen
        print(f"Deposit successful to account {self._account_id}. Updated balance: {self.get_balance()}")
    # Getter to get the value of fee
    def get_fee(self):
        return self.__fee

    # Setter to get the value for fee
    def set_fee(self, new_fee):
        self.__fee = new_fee



# Input the number of comment
n = int(input())

# Create an empty list which will save all the account of each peron to check whether it exists or not
List_account = []

# Consider n lines
for _ in range(n):
    # Declare for each line
    one_line = list(input().split())

    # If this line just have two elements, it will execute the period of create new account for a person
    if len(one_line) == 2:
        # Create account object
        Accountant = CheckingAccount(one_line[0], int(one_line[1]))

        # Add it to the list
        List_account.append(Accountant)

        # Print to the screen if the add process generate successfully
        print(f"Account {Accountant.get_account_id()} created with balance: {Accountant.get_balance()}")
    else:
        # Set the value for check exist to false, if it exists, this value will become true and remain false in other hand
        check_exist = False
        # Compare the existing with the List_account
        for i in range(len(List_account)):
            # If exists, the check exist will become true
            if List_account[i].get_account_id() == one_line[0]:
                check_exist = True
                # Implement two operations, deposit and withdraw
                if one_line[1] == "deposit":
                    # Depositing
                    List_account[i].deposit(int(one_line[2]))
                else:
                    # Withdrawing
                    List_account[i].withdraw(int(one_line[2]))
        if not check_exist:
            # If it does not exist, it will print the report to the screen
            print("Account does not exist.")

