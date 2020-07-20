# 1.
# import math

# class Circle():
#     def __init__(self, radius = 1):
#         self.radius = radius

#     def perimeter(self):
#         circumference = 2 * math.pi * self.radius
#         print(f'Circumference of the circle is {circumference}.')

#     def area(self):
#         area = math.pi * self.radius * self.radius
#         print(f'The area of the cirlce is {area}.')

# myCircle = Circle(2)
# myCircle.perimeter()
# myCircle.area()

# 2.

# the_list = ["Hello", "Apple", "Chair", "Follow"]

# class MyList():
#     def __init__(self, check_list):
#         self.check_list = check_list
    
#     def reverse_list(self):
#         self.check_list.reverse()
#         print(self.check_list)

#     def sorted_list(self):
#         my_sort = sorted(self.check_list)
#         print(my_sort)

#     # list comprehension

# tomers_list = MyList(the_list)
# tomers_list.reverse_list()
# tomers_list.sorted_list()

# 3.
import random

class QuantumParticle():
    def __init__(self, position, momentum, spin):
        self.position = position
        self.momentum = momentum
        self.spin = spin

    def position(self):
        pos = randint(1, 10000)

    def momentum(self):
        move = random.uniform(0, 1)
    
    def spin(self):
        spins = random.choice([0.5, -0.5])