from exercise2 import Dog
import random

class PetDog(Dog):
    def __init__(self, name, age, weight):
        super().__init__(name, age, weight)
        self.trained = False

    def train(self):
        print(self.bark())
        self.trained = True

    def play(self, *args):
        dog_names = ", ".join(args)
        print(f"{dog_names} all play together")

    def do_a_trick(self):
        if self.trained:
            trick_options = [
                f"{self.name} does a barrel roll",
                f"{self.name} stands on his back legs",
                f"{self.name} shakes your hand",
                f"{self.name} plays dead"
            ]
            print(random.choice(trick_options))
        else:
            print(f"{self.name} needs to be trained first!")


dog1 = PetDog("Chewy", 7, 5)
dog2 = PetDog("Rex", 8, 12)

dog1.train()
dog1.do_a_trick()
dog1.play("Chewy", "Rex")