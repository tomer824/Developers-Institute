# 1.

# 3 <= 3 < 9 = True
# 3 == 3 == 3 = True
# bool(0) = False
# bool(5 == "5") = False
# bool(4 == 4) == bool("4" == "4") = True
# bool(bool(None)) = False

# x = (1 == True)
# y = (1 == False)
# a = True + 4
# b = False + 10

# print("x is", x)
# print("y is", y)
# print("a:", a)
# print("b:", b)

# 2.

# a = input("Enter letter a: ")
# b = input("Enter letter b: ")

# if a > b:
#     print("Hello World")

# 3.

# season = input("Enter the number of a month from 1 - 12: ")
# season = int(season)
# if season < 1 and season > 12:
#     print("That is not a valid input")
# else:
#     if season == 1 or season == 2 or season == 12:
#         print("You are in Winter")
#     elif season == 3 or season == 4 or season == 5:
#         print("You are in Spring")
#     elif season == 6 or season == 7 or season == 8:
#         print("You are in summer")
#     else:
#         print("You are in Autumn")

# 4.

# my_text = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."
# print(len(my_text))

# 5.

not_a = input("Please enter a long string without useing the letter \"a\"")
# failed = False

# for letter in not_a:
#     if letter != "a":
#        continue            
#     else:
#         print("You used the letter \"a\"")
#         failed = True
#         break

# if failed == False:
#     print(f"You succeeded to write a sentence with {len(not_a)} charachters.")

if "a" in not_a:
    print("You used the letter \"a\"")
else: print(f"You succeeded to write a sentence with {len(not_a)} charachters.")