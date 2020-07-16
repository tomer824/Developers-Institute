# 1. 

# class Pets():
#     animals = []
#     def __init__(self, animals):
#         self.animals = animals

#     def walk(self):
#         for animal in self.animals:
#             print(animal.walk())

# class Cat():
#     is_lazy = True

#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def walk(self):
#         return f'{self.name} is just walking around'

# class Bengal(Cat):
#     def sing(self, sounds):
#         return f'{sounds}'

# class Chartreux(Cat):
#     def sing(self, sounds):
#         return f'{sounds}'

# class Siemese(Cat):
#     def sing(self, sounds):
#         return f'{sounds}'


# c1 = Bengal("Michael", 15)
# c2 = Chartreux("Sarah", 20)
# c3 = Siemese("Raquel", 10)

# my_cats = [c1, c2, c3]

# my_pets = Pets(my_cats)

# my_pets.walk()


# 2.

class BankAccount():
    def __init__(self, owner, balance = 0):
        self.owner = owner
        self.balance = balance
    
    def deposit(self):
        twenty = int(input("How many $20 bills would you like to deposit? ")) * 20
        fifty = int(input("How many $50 bills would you like to deposit? ")) * 50
        hundred = int(input("How many $100 would you like to deposit? ")) * 100
        total = twenty + fifty + hundred
        if total > 0:
            self.balance += total
            print(self.balance)
            deposit_more = input("Would you like to deposit more, enter y or n? ")
        if deposit_more == "y":
            self.deposit()
            return self.balance
        else:
            print("Thank you for coming, have a nice day. ")

    
    def withdraw(self, cash_back):
        if cash_back % 50 == 0 or cash_back % 20 == 0 and cash_back <= self.balance:
            self.balance -= cash_back
            return self.balance
        elif cash_back % 50 != 0 or cash_back % 20 != 0:
            print("This machine can only provide $20 and $50 bills.")
        else:
            print("You don't have enough money in your account for that withdrawal.")
        
    
class Owner(BankAccount):
    def __init__(self, owner, balance, cc_num, password):
        super().__init__(owner, balance)
        self.cc_num = cc_num
        self.password = password
    
    def check_owner_info(self, user_cc_num, user_password):
        for i in range(2):
            if user_password != self.password and i == 0:
                user_password = int(input("Please reenter your password: "))
            elif self.password == user_password:
                answer = input("Would you like to Deposit or to Withdraw? ")
                if answer.lower() == "deposit":
                    self.deposit()
                    return
                elif answer.lower() == "withdraw":
                    cash_back = int(input("How much would you like to withdraw? "))
                    self.withdraw(cash_back)
                    return
                else:
                    cash_back = int(input("I don't understand. Please try again. How much would you like to withdraw? "))
                    self.withdraw(cash_back)
                    return

            else:
                user_cc_num = None
                return "Your credit card has been eaten by the machine!"

tomer = Owner("Tomer", 100, 123456, 987654)
tomer.check_owner_info(123456, 987654)