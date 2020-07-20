# 1.

# big = int(input("Please enter a number: "))

# num2 = int(input("Please enter a number: "))
# if big < num2:
#     big = num2

# num3 = int(input("Please enter a number: "))
# if big < num3:
#     big = num3

# print(big)

# 2.

# alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p" , "q" , "r", "s", "t", "u", "v", "w", "x", "y", "z"]

# for vowels in alphabet:
#     if vowels == "a" or  vowels == "e" or vowels == "e" or vowels == "i" or vowels == "o" or vowels == "u":
#         print(f"{vowels} is a vowel")
#     else:
#         print(f"{vowels} is a consonant")

# 3.

# my_list = ["apple", "orange", "banana", "orange", "kiwi"]

# print(my_list.index("orange"))

# 4. 

# list1 = ["hello "]
# list2 = ["world"]

# list1.extend(list2)
# list1 = ''.join(list1)
# print(list1)

# 5.

# original_list = [("Tom", 19, 80), ("John", 20, 90), ("Jony", 17, 91), ("Jony", 17, 93), ("Json", 21, 85)]
# new_list = sorted(original_list, key=lambda tup: (tup[0], tup[1], tup[2]))
# print(new_list)

# 6.

# name = input("What is your name? ")
# waitress = input("What is your waitress name? ")
# item_ordered = input("What would you like to order? ")
# price = float(input("How much does the item cost? "))
# num = int(input("How many would you like to order? "))
# discount = int(input("How much is the discount? "))
# total = (num * price + discount) + ((num * price + discount) * 0.17)
# print(f"""Hello {name}, \n Your waitress today was {waitress}. \n 
# You Ordered:    {item_ordered}\n Amount :    {num}\n with {discount} discount.\n
# Your total today with VAT is {total}.\n
# Thank you for your patronage. """)

# 7.

# from random import randint
# num = randint(1, 9)
# print(num)

# 8.

# for num in range(1, 1000001):
#     print(num)

# 9.

# low = min(1, 2)
# high = max(1, 1000000)
# my_list = []
# for num in range(low, high):
#     my_list.append(num)

# total = sum(my_list)
# print(total)
    

