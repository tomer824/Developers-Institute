# 3.

# print("Hello World \n" * 5 + "I love Python \n" * 5)

# 4.

num = input("Please enter a number: ")
print(int(num))
for i in range(1, 5):
    num = int(num * i) + int(num)
    print(num)