# 1.

# import math

# cars = 100
# drivers = 30
# passengers = 100

# if cars > drivers:
#     print(f"There are {drivers} available cars today")
# else:
#     print(f"There are {cars} available cars today.")

# f"There are {drivers} registerdd on the application."

# if cars > drivers:
#     empty_cars = cars - drivers
#     print(f"There are {empty_cars} empty cars today")

# if cars >= drivers:
#     num_pass = drivers * 4
#     print(f"We can transport {num_pass} passengers today.")
# else:
#     num_pass = cars * 4
#     print(f"We can transport {num_pass} passengers today.")

# if passengers / drivers > 4:
#     average_passengers = 4
#     print("There are 4 passengers in each car.")
# else: 
#     average_passengers = round((passengers / drivers), 2)
#     print(f"There is an average of {average_passengers} passengers in each car.")


# 2.

# import re
# password = input("Enter string to test: ")
# # Add any special characters as your wish I used only #@$
# if re.match(r"^(?=.*[\d])(?=.*[A-Z])(?=.*[a-z])(?=.*[@#$])[\w\d@#$]{6,12}$", password):
#     print ("match")
# else:
#     print ("Not Match")

# 3 / 4.

# Ask the user for his full name (example: “John Doe”), and check the validity of his answer:
# The name should contain only letters.
# The name should contain only one space.
# The first letter of each name should be upper cased.



name = input("Please enter your full name: ")

if all(letter.isalpha() or letter.isspace() for letter in name):
	name_lists = name.split(" ")
	if len(name_lists) == 2:
		if name_lists[0][0].isupper() and name_lists[0][0].isupper():
			print("yes")