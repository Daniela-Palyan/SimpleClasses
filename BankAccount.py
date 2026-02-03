# Create a class BankAccount with account_number and balance. Add a method deposit(amount) to increase the balance
# Modify the BankAccount class to include a withdraw(amount) method that reduces the balance if there are enough funds.

class BankAccount:
    def __init__(self, account_number, balance):
        if not isinstance(balance, (int, float)):
            raise TypeError("Your balance must be a number!")
        if balance < 0:
            raise ValueError("Your balance must be a positive number!")

        self.__account_number = account_number
        self.__balance = balance

    def get_account_number(self):
        return self.__account_number
    
    def get_balance(self):
        return self.__balance
    
    def deposit(self, amount):
        if not isinstance(amount, (int, float)):
            raise TypeError("Your amount must be a number!")
        if amount < 0:
            raise ValueError("Your amount must be a positive number!")
        
        self.__balance += amount

    def withdraw(self, amount):
        if not isinstance(amount, (int, float)):
            raise TypeError("Your amount must be a number!")
        if amount < 0:
            raise ValueError("Your amount must be a positive number!")
        
        if self.get_balance() < amount:
            return "Not enough funds on balance!"

        self.__balance -= amount

    

ba1 = BankAccount(2739102378, 6700)
print(ba1.get_account_number(), ba1.get_balance())

ba1.deposit(300)
print(ba1.get_account_number(), ba1.get_balance())


ba1.withdraw(1800)
print(ba1.get_account_number(), ba1.get_balance())