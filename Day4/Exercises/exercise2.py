class Dog:
    def __init__(self, name, age, weight):
        self.name = name
        self.age = age
        self.weight = weight

    def bark(self):
        return f"{self.name} is barking"

    def run_speed(self):
        return self.weight / self.age * 10

    def fight(self, other_dog):
        self_speed = self.run_speed() * self.weight
        other_speed = other_dog.run_speed() * other_dog.weight
        if self_speed > other_speed:
            return f"{self.name} won the fight!"
        elif other_speed > self_speed:
            return f"{other_dog.name} won the fight!"
        else:
            return "It's a draw!"


dog1 = Dog("Barbos", 13, 15)
dog2 = Dog("Max", 3, 22)
dog3 = Dog("Kerber", 7, 10)

print(dog1.bark())  
print(dog2.run_speed())
print(dog3.fight(dog1))
