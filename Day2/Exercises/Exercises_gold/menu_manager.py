class MenuManager:
    def __init__(self):
        self.menu = [
            {"name": "Soup", "price": 10, "spice": "B", "gluten": False},
            {"name": "Hamburger", "price": 15, "spice": "A", "gluten": True},
            {"name": "Salad", "price": 18, "spice": "A", "gluten": False},
            {"name": "French Fries", "price": 5, "spice": "C", "gluten": False},
            {"name": "Beef bourguignon", "price": 25, "spice": "B", "gluten": True}
        ]

    def add_item(self, name, price, spice, gluten):
        new_item = {"name": name, "price": price, "spice": spice, "gluten": gluten}
        self.menu.append(new_item)
        print(f"{name} has been added to the menu.")

    def update_item(self, name, price, spice, gluten):
        for item in self.menu:
            if item["name"] == name:
                item["price"] = price
                item["spice"] = spice
                item["gluten"] = gluten
                print(f"{name} has been updated.")
                break
        else:
            print(f"{name} is not in the menu.")

    def remove_item(self, name):
        for item in self.menu:
            if item["name"] == name:
                self.menu.remove(item)
                print(f"{name} has been removed from the menu.")
                break
        else:
            print(f"{name} is not in the menu.")

    def print_menu(self):
        print("Current Menu:")
        for item in self.menu:
            print(item)


menu_manager = MenuManager()

print("Initial Menu:")
menu_manager.print_menu()

print("\nAdding a new dish:")
menu_manager.add_item("Pizza", 20, "A", True)

print("\nUpdating Salad:")
menu_manager.update_item("Salad", 20, "B", True)

print("\nRemoving French Fries:")
menu_manager.remove_item("French Fries")

print("\nUpdated Menu:")
menu_manager.print_menu()



