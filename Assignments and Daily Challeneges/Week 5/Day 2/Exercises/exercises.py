# 1.

# class Human():

#     def __init__(self, name, age, gender):
#         self.name = name
#         self.age = age
#         self.gender = gender
#         self.eyes_color = "blue"

#     def talk(self):
#         print(f"{self.name}: bla bla bla")

# tomer = Human(name="Tomer", age = 25, gender = "M")
# print(tomer.name)
# print(tomer.age)
# print(tomer.gender)
# print(tomer.eyes_color)
# tomer.eyes_color = "Brown"
# print(tomer.eyes_color)

# tomer.talk()

# 2.

class Book():

    BEST_AUTHOR = "Victor Hugo"

    def __init__(self, text, title, author, genre):
        self.text = text
        self.title = title
        self.author = author
        self.genre = genre
    
    def read(self):
        sentences = self.text.split(". ")
        for s in sentences:
            print(s)

hp = Book(text = "some sentences. some other sentences dursleys.", title = "Harry Potter", author = "J.K. Rowling", genre = "Fantasy")

hp.read()
print(hp.BEST_AUTHOR)
print(Book.BEST_AUTHOR)

class American(Human):
    
    def amazed(self):
        print("It's amazing!")

tzivia = American(name="Tzivia", age=22, gender="F")

print(tzivia.name)
tsivia.talk()
tzivia.amazed()

# from math import pi
# class Book:
#     BEST_AUTHOR = "Victor Hugo"
#     def __init__(self, text, title, author, genre):
#         self.text = textls
#         self.title = title
#         self.author = author
#         self.genre = genre
#     def read(self):
#         sentences = self.text.split(". ")
#         for s in sentences:
#             print(s)
# hp = Book(text="some sentences. some other sentences about the dursleys.",
#           title="Harry Potter", author="J.K. Rowling", genre="Fantasy")
# hp.read()  # read(hp)
# print(hp.BEST_AUTHOR)
# print(Book.BEST_AUTHOR)
# class Circle:
#     PI = pi
#     def __init__(self, radius):
#         self.r = radius
#     def area(self):
#         return Circle.PI * self.r ** 2
# c = Circle(radius=2)
# print(c.area())


# 4.

# class Student():
#     def __init__(self, name, school, major)
#     self.name = name
#     self.school = school
#     self.major = major

#     def set_gpa(self, gpa):
#         self.gpa = gpa

#     def compute_gpa(self, grades):
#         self.gpa = sum(grades) / len(grades)

# class PhDStudent(Student):
#     def__init__(self, name, school, major, supervisor):
#         super().__initi(name, school, major)
#         self.supervisor = supervisor