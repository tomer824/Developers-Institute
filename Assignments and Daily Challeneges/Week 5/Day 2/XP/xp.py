# 1.

members = [ {'name':'Michael','age':35,'gender':'Male','is_child':False}, {'name':'Sarah','age':32,'gender':'Female','is_child':False} ]

class Family():
    def __init__(self, members, last_name):
        self.members = members
        self.last_name = last_name
                 
    def born(self, name, gender):
        new_child = {"name" : name, "age" : 0, "gender" : gender, "is_child" : True}
        self.members.append(new_child)
        print("Congratulations")
    
    def is_18(self, name):
        for member_dict in self.members:
            if member_dict["name"] == name:
                if member_dict["age"] > 18:
                    return True
                else:
                    return False
    
    def __str__(self):
        return f"This is the {self.last_name} family. "

    def __repr__(self):
        return f"I am different"

    def __int__(self):
        return len(self.members)

goldstein = Family(members, "Goldstein")
smith = Family(members, "Smith")
print(goldstein.members)

# 2.
from random import randint

class TheIncredibles(Family):
     
    def use_power(self, name):
        for member_dict in self.members:
            if member_dict["name"] == name:
                if member_dict["age"] > 18:
                    print(f'{member_dict["name"]} has incredible_presentation().')
                    self.member_dict["power"] = members.incredible_presentation()
                else:
                    raise Exception("You have no power here!")
    
    def incredible_presentation(self):
        super_powers = ["X-Ray Vision", "Super Strength", "Bullet Proof", "Super Speed"]
        item = randint(0, 4)
        for powers in super_powers:
            return powers[item]


incredibles = TheIncredibles(members, "Goldstein")
