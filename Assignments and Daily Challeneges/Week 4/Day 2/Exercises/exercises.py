# Exercise 1.
# getting index 20 and changing it to 200

# list = [5, 10, 15, 20, 25, 50, 20]

# index_20 = list.index(20)
# list[list.index_20] = 200
# print(list)

# # Exercise 2.

# aTuple = (10, 20, 30, forty)
# a, b, c, d = aTuple #unpacking the tuple

# Exercise 1 - Loops

# num = int(input("Give us a number: "))
# equation = []

# for multiplication in range(1,11):
#     equation.append(num*multiplication)

# print(equation)

# Exercise 2. - loops

# i = 0

# while i < 10:
#     print("Running...")
#     i += 1
# print("Stopping")

new_list = [1, 2, -1, 3, 4, -1]

while new_list:
    new_list.pop()
    print(new_list)
