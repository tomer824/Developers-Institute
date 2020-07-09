#1. 

# import random

# def get_random_temp(season):
#     if season == "winter":
#         return random.randint(-10, 16)
#     elif season == "fall" or season == "spring":
#         return random.randint(17, 27)
#     elif season == "summer":
#         return random.randint(28, 40)

# def main():
#     season = input("What season is it, winter, spring, summer or fall? ")
#     temp = get_random_temp(season)
#     print(f"The temperature right now is {temp} degress Celsius.")
#     if temp < 0:
#         print("Brrr, that freezing! Wear some extra layers today!")
#     elif temp >= 0 and temp < 16:
#         print("Quite chilly! Dont forget your coat.")
#     elif temp >=16 and temp <= 23:
#         print("I suggest you wear a light sweater today.")
#     elif  temp >= 24 and temp <= 32:
#         print("It should be a very nice day out today.")
#     else:
#         print("It will be very warm outside today. Wear lots of sunscreen.")

# main()

# 2.

def throw_dice():
    return random.randint(1, 6)


roll_count = 1
total_count = 1

rolls_to_double = []

def throw_until_doubles():
    roll1 = throw_dice()
    roll2 = throw_dice()
    if roll1 != roll2:
        roll_count += 1
        throw_until_doubles()
    else:
        full_count = roll_count
        roll_count = 1
        return full_count

def main():
    throw_dice()

    print(f"It took a total of {total_count} to reach 100 doubles")