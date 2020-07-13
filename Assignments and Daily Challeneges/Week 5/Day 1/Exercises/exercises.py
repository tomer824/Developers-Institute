# 1.

# class Cat:
#     species = 'mammal'
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

# cat1 = Cat("Mickey", 7)
# cat2 = Cat("Sarah", 4)
# cat3 = Cat("Robert", 2)

# def oldest_cat(cat1, cat2, cat3):
#     oldest = cat1.age
#     if oldest < cat2.age:
#         oldest = cat2.age
#     elif oldest < cat3.age:
#         oldest = cat3.age
#     return oldest

# print(f"The oldest cat is {oldest_cat(cat1, cat2, cat3)} years old.")

# 2.

# class Dog():
#     def __init__(self, nameDog, heightDog):
#         self.name = nameDog
#         self.height = heightDog
#         self.talk()
#         self.jump()

#     def talk(self):
#         print(f"Woof, my name is {self.name}")
    
#     def jump(self):
#         print(f"The dog is {self.height * 2} cm tall")

# Davids_dog = Dog("Rex", 50)

# Sarahs_dog = Dog("Teacup", 20)

# 3.

# class Song():
#     def __init__(self, lyrics):
#         self.lyrics = lyrics

#     def sing_me_a_song(self):
#         for line in self.lyrics:
#             words = line.split(" ")
#             for word in words:
#                 print(word)

# happy_birthday = Song(["Happy Birthday to you", "How old are you now"])
# happy_birthday.sing_me_a_song()

# 4.

class Zoo():
    def __init__(self, zoo_name):
        self.zoo_name = zoo_name
        self.animals = []
        self.animals_in_pens = []
    
    def add_animal(self, new_animal):
        if new_animal not in self.animals:
            self.animals.append(new_animal)
    
    def get_animals(self):
        for animal in self.animals:
            print(animal)
    
    def sell_animals(self, animal_sold):
        print(f"Goodbye {animal_sold}")
        self.animals.remove(animal_sold)

    def get_pen_number(self, animal):
        return ord(animal[0].upper()) - 64 
    
    def place_animal_in_pen(self, number, animal):
        if number in self.animals_in_pens:
            self.animals_in_pens[number].append(animal)   
        else:
            self.animals_in_pens[number] = animal
        return self.animals_in_pens
        
    def sort_animal(self):
        for animal in self.animals:
            number = self.get_pen_number(animal)
            print(self.place_animal_in_pen(number, animal))


ramatGanSafari = Zoo("The National Israel Safari")

extraanimals = ["Lion", "Tiger", "Moose", "Lion", "Turtle", "Lemur", "Ape"]
for animal in extraanimals:
    ramatGanSafari.add_animal(animal)

ramatGanSafari.get_animals()

ramatGanSafari.sell_animals("Moose")

ramatGanSafari.get_animals()

ramatGanSafari.sort_animal()