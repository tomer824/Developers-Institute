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
    
    def deposit(self, cash):
        if cash > 0:
            self.balance += cash
        return self.balance
    
    def withdraw(self, cash_back):
        if cash_back <= self.balance:
            self.balance -= cash_back
        return self.balance
    
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
                return "Would you like to Deposit or to Withdraw?"
            else:
                return "Your credit card has been eaten by the machine!"



    #             return "Would you like to Deposit or to Withdraw"
    #         else:
    #             count += 1
    #             print("Please try again")
    #             check_owner_info_2()
    #             if count > 1:
    #                 return "Your card has been eaten by the machine" and user_cc_num = ""
    
    # def check_owner_info_2(self, cc_num, password)
    #         if user_password != self.password:
    #             return "Would you like to Deposit or to Withdraw"
    #         else:
    #             return "Your card has been eaten by the machine" and user_cc_num = ""

