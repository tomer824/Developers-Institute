# 1.

# def display_message():
#     print("I am learning python in this lesson")

# display_message()

# 2.

# def favorite_book(title):
#     print(f"One of my favorite books is {title}.")

# favorite_book("Alice in Wonderland")

# 3.

# def make_shirt(size = "L", text = "I love Python"):
#     if size == "L" or size == "M":
#         text = "I am the default message for L and M"
#     else:
#         text = "I am the default message for everything else"        
#     print(f"The shirt is a size {size} and the message is {text}.")

# make_shirt("L", "This is my new shirt")
# make_shirt(size = "S", text = "My shirt shrank")


# 4.

magicians = ["Houdini", "Harry Potter", "Magic Man"]

def show_magicians(magicians):
    for name in magicians:
        print(name)

def make_great(magicians):
    for name in range(len(magicians)):
        magicians[name] = magicians[name] + " the Great"

show_magicians(magicians)
make_great(magicians)

show_magicians(magicians)

# 5.

# def describe_city(city, country = "Israel"):
#     print(f"{city} is in {country}")

# describe_city("Jerusalem")
# describe_city("Tel Aviv")
# describe_city("New York", "United States")

# 6.

# def get_age(year, month, day):
#     current_year = 2020
#     current_month = 7
#     current_day = 8
#     age = current_year - year
#     if current_month > month:
#         age -= 1
#     elif current_month == month:
#         if current_day > day:
#             age -=1
#     return age
    
# def can_retire(gender, date_of_birth):
#     day, month, year = date_of_birth.split("/")
#     age = get_age(int(year),int(month), int(day))
#     if gender == "male" and age > 64:
#         print("True")
#         return True
#     elif gender == "female" and age > 61:
#         print("True")
#         return True
#     else:
#         print("False")
#         return False

# gender = input("What is your gender, male or female? ")
# dob = input("Please enter your date of birth as DD/MM/YYYY ")

# can_retire(gender, dob)