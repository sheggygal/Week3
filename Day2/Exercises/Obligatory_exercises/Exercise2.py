class Dog:
    def __init__(self, name, height):
        self.name = name
        self.height = height

    def bark(self):
        print(f"{self.name} goes woof!")

    def jump(self):
        jump_height = self.height * 2
        print(f"{self.name} jumps {jump_height} cm high!")


davids_dog = Dog("Rex", 50)

print("David's dog details:")
print("Name:", davids_dog.name)
print("Height:", davids_dog.height, "cm")
davids_dog.bark()
davids_dog.jump()

sarahs_dog = Dog("Teacup", 20)

print("\nSarah's dog details:")
print("Name:", sarahs_dog.name)
print("Height:", sarahs_dog.height, "cm")
sarahs_dog.bark()
sarahs_dog.jump()

if davids_dog.height > sarahs_dog.height:
    print("\nThe bigger dog is:", davids_dog.name)
elif davids_dog.height < sarahs_dog.height:
    print("\nThe bigger dog is:", sarahs_dog.name)
else:
    print("\nBoth dogs are of the same height.")


