# 1.

# fruits = input("What are your favorite fruits, seperate multiples by space? ")
# fruits = fruits.split(" ")
# which_fruit = input("Please enter a fruit: ")

# if which_fruit in fruits:
#     print("You chose one of your favorite fruits! Enjoy!")
# else:
#     print("You chose a new fruit. I hope you enjoy it too!")

# new_list = ""
# for i, fruit in enumerate(fruits):
#     if i != len(fruits) - 1:
#         new_list = new_list + fruit + " and "
#     else:
#         new_list = new_list + fruit
# print(new_list)

# 2.

# car_man = "Volkswagen, Toyota, Ford Motor, Honda, Chevrolet"
# car_list = car_man.split(", ")
# print(len(car_list))
# print(list(reversed(sorted(car_list))))

# count_o = 0
# count_i = 0
# for car in car_list:
#     if "o" in car:
#         count_o += 1
#     elif "i" not in car:
#         count_i += 1

# print(f"There are {count_o} manufacturers with the letter o.")
# print(f"There are {count_i} manufacturers without the letter i.")

# car_set = set(car_list)

# 3.

# my_list = ["1", "2", "3"]
# my_list.insert(1, "7")
# print(my_list)

# 4.

# Write a program that counts the number of spaces in a string.
# Hint: use a function

# string = "Hello world i am here"

# print(string.count(" "))

# 5.

# Write a program that calculates the number of upper case letters and lower case letters in a string.
# Hint: use a function

# string = "HellO WoRlD I am HERe"

# count_lower = sum(map(str.islower, string))
# print(count_lower)

# count_upper = sum(map(str.isupper, string))
# print(count_upper)