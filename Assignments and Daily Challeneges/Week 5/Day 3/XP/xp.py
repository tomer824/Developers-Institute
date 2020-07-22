# 1.

# class Currency():
#     def __init__(self, value, currency):
#         self.value = float(value)
#         self.currency = currency

#     def __repr__(self):
#         return f"The value of your {self.currency} is {self.value}."

#     # * currency + 5
#     # * currency  +  another_currency  (if they have the same label, otherwise raise an error)
#     # ----

#     def __add__(self, other_currency):
#         if self.currency == other_currency.currency:
#             print(self.value + other_currency.value)
#         else:
#             raise ValueError "Not the same currency."

# #     * currency += 5
# #     * currency += another_currency  (if they have the same label, otherwise raise an error)
# #     ----

#     def __iadd__(self, other_currency):
#         if self.currency == other_currency.currency:
#             print(self.value += 5)
#         else:
#             raise ValueError "Not the same currency."

# #     * currency - 5
# #     * currency - another_currency  (if they have the same label, otherwise raise an error)
# #     ----

#     def __sub__(self, other_currency):
#         if self.currency == other_currency.currency:
#             print(self.value - other_currency.value)
#         else:
#             raise ValueError "Not the same currency."

# #     * currency -= 5
# #     * currency -= another_currency  (if they have the same label, otherwise raise an error)
# #     ----

#     def __isub__(self, other_currency):
#         if self.currency == other_currency.currency:
#             print(self.value -=  5)
#         else:
#             raise ValueError "Not the same currency."


# #     * currency  * 5
# #     * currency  *  another_currency  (if they have the same label, otherwise raise an error)
# #     ----
#     def __mul__(self, other_currency):
#         if self.currency == other_currency.currency:
#             print(self.value * other_currency.value)
#         else:
#             raise ValueError "Not the same currency."

# #     * currency *= 5
# #     * currency *= another_currency  (if they have the same label, otherwise raise an error)
# #     ----

#     def __imul__(self, other_currency):
#         if self.currency == other_currency.currency:
#             print(self.value *=  5)
#         else:
#             raise ValueError "Not the same currency."

# #     * currency / 5
# #     * currency / another_currency  (if they have the same label, otherwise raise an error)
# #     ----

#     def __div__(self, other_currency):
#         if self.currency == other_currency.currency:
#             print(self.value / other_currency.value)
#         else:
#             raise ValueError "Not the same currency."

# #     * currency /= 5
# #     * currency /= another_currency  (if they have the same label, otherwise raise an error)
# #     ----

#     def __idiv__(self, other_currency):
#         if self.currency == other_currency.currency:
#             print(self.value /=  5)
#         else:
#             raise ValueError "Not the same currency."

# #     * Write a program that prints the list of methods for any type of objects.

# help()

# dollar = Currency(10, "Dollars")
# dollar2 = Currency(15, "Dollars")
# dollar3 = Currency(20, "Shekels")

# print(dollar.__add__(dollar2))

# 2.

# The goal is to create a class that represents a simple circle.
# A Circlecan be defined by either specifying the radius or the diameter. The user can query the circle for either its radius or diameter.

# Other abilities of a Circle instance:

# Compute the circle’s area
# Print the circle and get something nice
# Be able to add two circles together
# Be able to compare two circles to see which is bigger
# Be able to compare to see if there are equal
# Be able to put them in a list and sort them

import math

class Circle():
    def __init__(self, name, radius):
        self.name = name
        self.radius = radius
        self.area = math.pi * self.radius**2

    def __add__(self, other_circle):
        both_circles = self.area + other_circle.area
        return both_circles

    def __gt__(self, other_circle):
        if self.area > other_circle.area:
            return True
        return False
    def __eq__(self, other_circle):
        if self.area == other_circle.area:
            return True
        return False

def sort(*circles):
    circle_list = []
    for circle in circles:
        circle_list.append(circle)
    circle_list.sort()
    return circle_list