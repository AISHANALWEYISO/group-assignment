# Basic: Create a class called Car with attributes brand and color. 
# Instantiate an object of the Car class and print its attributes.
class Car:
    def __init__(self, brand, color):
        self.brand = brand
        self.color = color

p1 = Car("Toyota", "Blue")
print(p1.brand)
print(p1.color)
 
# Intermediate: Add a method called start_engine to the Car class that prints 
# a message saying the engine of the car has started. Create an instance of Car and call the method.   
class Car:
    def __init__(self,start_engine):
        self.start_engine = start_engine

start = Car('The car engine has started')
print(start.start_engine)

# Advanced: Create a class called BankAccount with attributes account_number and balance. Add methods to:
# Deposit an amount.
# Withdraw an amount (only if sufficient balance exists).
# Print the account balance.

class BankAccount:
    def __init__(self,account_number,balance=0):
        self.account_number  = account_number
        self.balance  = balance

    def deposit(self,amount):
        if amount > 0:
            self.amount += amount
            print(f'You have deposited {amount} and current account balane is {self.balance}')
        
        else:
            print(f'Please deposit an amount')

    def withdraw (self, amount):
        if amount >0:
            if self.balance >= amount:
                self.balance -= amount
                print(f'Withdraw {amount}. Current balaance {self.balance}')
            else:
                print('Insufficient balance')

        else:
            print('Withdrawal amount')

    def print_balance(self):
        print(f'Account {self.account_number} balance {self.balance}')

account = BankAccount(255336)
account.deposit(50000)
account.withdraw(1000)
account.print_balance()

# Challenge: Implement a class called Library that manages a collection of books. Each book has a title, author, and available status. The Library class should have methods to:
# Add a book to the library.
# Remove a book from the library.
# Check if a book is available by title.
# Borrow a book (mark it as unavailable if it’s available).
# Return a book (mark it as available again if it was borrowed).
