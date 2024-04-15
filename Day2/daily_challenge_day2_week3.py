class Farm:
    def __init__(self, name):
        self.name = name
        self.animals = {}

    def add_animal(self, animal_type, count=1):
        if animal_type in self.animals:
            self.animals[animal_type] += count
        else:
            self.animals[animal_type] = count

    def get_info(self):
        info = f"{self.name}'s farm\n"
        for animal, count in self.animals.items():
            info += f"{animal} : {count}\n"
        info += "E-I-E-I-O!"
        return info

    def get_animal_types(self):
        return sorted(self.animals.keys())

    def get_short_info(self):
        animal_types = self.get_animal_types()
        num_types = len(animal_types)
        if num_types == 1:
            animals_str = animal_types[0]
        elif num_types == 2:
            animals_str = f"{animal_types[0]} and {animal_types[1]}"
        else:
            animals_str = ", ".join(animal_types[:-1]) + f", and {animal_types[-1]}"

        animal_plural = "s" if num_types > 1 else ""

        return f"{self.name}'s farm has {animals_str}{animal_plural}."


macdonald = Farm("McDonald")
macdonald.add_animal('cow', 5)
macdonald.add_animal('sheep')
macdonald.add_animal('sheep')
macdonald.add_animal('goat', 12)
print(macdonald.get_info())

print("\nAnimal types in the farm:", macdonald.get_animal_types())
print(macdonald.get_short_info())

