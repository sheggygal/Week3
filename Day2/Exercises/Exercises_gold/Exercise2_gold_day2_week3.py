import random

class MyList:
    def __init__(self, letters):
        self.letters = letters

    def reverse_list(self):
        return list(reversed(self.letters))

    def sorted_list(self):
        return sorted(self.letters)

    def generate_random_list(self):
        return [random.randint(1, 100) for _ in range(len(self.letters))]


my_list = MyList(['a', 'b', 'c', 'd', 'e'])

print("Original List:", my_list.letters)
print("Reversed List:", my_list.reverse_list())
print("Sorted List:", my_list.sorted_list())
print("Random List:", my_list.generate_random_list())



