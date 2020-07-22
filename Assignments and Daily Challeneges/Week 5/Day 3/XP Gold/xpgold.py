# 1.

# class Warrior():
#     def __init__(self, name):
#         self.name = name
#         self.lifepoints = 50
#         print("Grrrr...")

#     def roar(self):
#         print(f"{self.name} is screaming loudly!")
    
#     def attack(self, other_person):
#         other_person.lifepoints -= 10
#         print(f"{other_person.name} has lost 10 life points.")

# class Sorcerer():
#     def __init__(self, name):
#         self.name = name
#         self.lifepoints = 50
#         print("Wooba Lubba dub dub !")

#     def curse(self, other_person):
#         print(f"{self.name} curses {other_name.name}")

# class Drood():
#     def __init__(self, name):
#         self.name = name
#         self.lifepoints = 50
#         print("Hello World")

#     def heal(self):
#         self.lifepoints += 10
#         print(f"{self.name} has healed himself by 10 life points.")

#     def heal_other(self, other_person):
#         other_person.lifepoints += 10
#         print(f"{self.name} has healed {other_person.name} by 10 life points.")


# 2.

num = int(input("Please enter a number between 1 - 100: "))

def outer_function(number):

    def wrapper(*args):
        return number(*args)
    return wrapper

@outer_function
def bigger(num):
    if num > 50:
        return True
    return False

@outer_function
def smaller(num):
    if num < 50:
        return True
    return False

@outer_function
def equal(num):
    if num == 50:
        return True
    return False
