class Farm:
    def __init__(self, farmer):
        self.animals = []

    def add_animal(animal, amount):
        self.animals.append({animal : amount})

macdonald = Farm("MacDonald")
farm_animals = [("cow", 5),("goat", 12),("Sheep", 2)]

for animal in farm_animals:
    macdonald.add_animal()


print(farm_animals)