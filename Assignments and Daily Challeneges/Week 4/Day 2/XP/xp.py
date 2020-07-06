# 1.

# my_fav_numbers = set([1, 3,])
# my_fav_numbers.add(7)
# my_fav_numbers.add(9)
# my_fav_numbers.remove(9)

# friend_fav_numbers = set([5, 7])
# our_fav_numbers = my_fav_numbers.union(friend_fav_numbers)
# print(our_fav_numbers)

# 2.

# my_fav_numbers = (1, 3)
# my_fav_numbers += (7)
# my_fav_numbers += (9)
# my_fav_numbers -= (9)
# print(my_fav_numbers)

# 3.

# Float is for numbers with a decimal point - integer has no decimal point
# N/A - please re-review the question
# a = "1"
# float(a)

# i = 1.5
# while i <= 5:
#     print(i)
#     i += 0.5

# 4.

# for i in range(1, 21):
#     print(i)

# 5.

# toppings = input("What toppings would you like to add to your pizza? Enter done when finished: ").lower()
# while toppings != "done":
#     print("I'll add that topping to your pizza")
#     toppings = input("What toppings would you like to add to your pizza? Enter done when finished: ").lower()

# 6.

# family_age = [10, 5, 2, 26, 29]
# total = 0

# for age in family_age:
#     if age < 3:
#         total += 0
#     elif age > 2 and age < 13:
#         total += 10
#     else:
#         total += 15

# print(f"The total amount is {total}.")

# age = int(input("How old are you? "))
# allowed_list = []

# if age > 15 and age < 22:
#     allowed_list.append(age)
#     print("You are able to see the movie")
# else:
#     print("You are not allowed to the see movie")

# print(allowed_list)    

# 7.

# users = [13, 24, 56, 7, 16]
# i = 0

# for check in users:
#     if check < 16:
#         users.remove(users[i])
#     i += 1

# print(users)

# 8.

# basket = ["Banana", "Apples", "Oranges", "Blueberries"]

# basket.pop(0)
# basket.pop(-1)
# basket.append("Kiwi")
# basket.insert(0, "Apples")
# print(basket)
# basket_count = basket.count("Apples")
# print(basket_count)
# basket = []

# 9.

# basket = ["Banana", "Apples", "Oranges", "Blueberries"]
# i = 0

# while i < len(basket):
#     print(basket[i])
#     i += 1

# 10.

# i = 0
# basket = ["Banana", "Apples", "Oranges", "Blueberries"]

# while i < len(basket):
#     if i % 2 == 0:
#         print(basket[i])
#     i += 1
