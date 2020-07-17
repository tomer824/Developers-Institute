class MenuManager():
    def __init__(self, menu):
        self.menu = [
            {"name": "soup", "price": 10, "spice_level": "b", "gluten_index": False},
            {"name": "hamburger", "price": 15, "spice_level": "a", "gluten_index": True},
            {"name": "salad", "price": 18, "spice_level": "a", "gluten_index": False},
            {"name": "french_fries", "price": 5, "spice_level": "c", "gluten_index": False},
            {"name": "beef_bourguignon", "price": 25, "spice_level": "b", "gluten_index": True}
        ]
    
    def add_item(self, name, price, spice, gluten):
        self.menu.append({"name" : name, "price" : price, "spice_level" : spice, "gluten_index" : gluten})
    
    def update_item(self, name, price, spice, gluten):
        dish2 = {"name" : name, "price" : price, "spice_level" : spice, "gluten_index" : gluten}
        for dish in self.menu:
            if dish["name"] == name:
                dish.update(dish2)
                return
        print("That dish isn't in the menu.")
    
    def remove_item(self, name):
        for dish in self.menu:
            if dish["name"] == name:
                self.menu.remove(dish)
                print(self.menu)
                return
        print("That dish isn't in the menu.")

