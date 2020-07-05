import random

num = input("Please enter a 10 charachter string: ")


if len(num) != 10:
    num = input("Sorry, that was not 10 characters, please try again: ")
else:
    print(f"The first letter is {num[0]}")
    print(f"The last letter is {num[-1]}")
    for i in range(len(num)+1):
        print(num[:i])

shuffled = list(num)
random.shuffle(shuffled)
shuffled = ''.join(shuffled)
print(shuffled)