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
    
	def __init__(self, card_number, pin_number=12345):
		self.balance = 0
		self.card_number = card_number
		self.pin_number = pin_number

    def deposit(self, amount):
        if amount >= 0:
            self.balance += amount
            return True
        return False
​
	def withdraw(self, amount):
		if amount <= self.balance and checkBills = True:
			self.balance -= amount
			return amount
		return False
​
	def check_info(self, card_number, pin_number):
		if card_number == self.card_number and pin_number == self.pin_number:
			return True
		return False
​
	def depositBills(self):
		ans = True
        total = 0
        while ans = True:
            twenty = int(input("How many twenties would you like to deposit? ")) * 20
            fifty = int(input("How many fifties would you like to deposit? ")) * 50
            hundred = int(input("How many hundreds would you like to deposit? ")) * 100
            total += sum(twenty, fifty, hundred)
            again = ("Would you like to make another deposit? ")
                if again = yes.lower():
                    ans = True
                else:
                    ans = False
        return total
​
	def checkBills(self, amount):
		if amount % 20 == 0 or amount % 50 == 0 
            return True
        elif amount - 50 < 0 and amount - 50 % 20 = 0):
            return true
        return False
​
​​
class Owner():
​
	def __init__(self, name):
		self.name = name
		print(f"{self.name} has been born")
​
​
	def open_account(self, card_number, pin_number):
		self.account = BankAccount(card_number, pin_number)
		print("Your account is ready")
​
​
	def deposit(self, amount):
		if self.authenticate():
			amount = self.depositBills()
			if self.account.deposit(amount):
				print(f"Deposit Successful. You new balance is: {self.account.balance}")
			else:
				print("Invalid Amount.")
		else:
			print("Your card has been eaten")
​
​
	def withdraw(self, amount):
		if self.authenticate():
			if self.account.withdraw(amount):
				print(f"Here is your: {amount}")
			else:
				print("Insufficient Balance")
		else:
			print("Your card has been eaten")
​
​
	def authenticate(self):
		for i in range(2):
			card_number = input("Enter your card number: ")
			pin_number = input("Enter your pin number: ")
			if self.account.check_info(card_number, pin_number):
				return True
			else:
				if i < 1:
					print("Invalid authentication. Please try again")
		return False

tomer = Owner("Tomer", 100, 123456, 987654)
tomer.check_owner_info(123456, 987654)