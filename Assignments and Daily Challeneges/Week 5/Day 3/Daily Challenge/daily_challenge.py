my_string = input("Please enter your word or set of numbers: ")

if str(my_string) == str(my_string)[::-1]:
    print("This is a palindrome.")
else:
    print("Fail")