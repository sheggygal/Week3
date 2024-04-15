class Cat:
    def __init__(self, cat_name, cat_age):
        self.name = cat_name
        self.age = cat_age


cat1 = Cat("Chewbaka", 11)
cat2 = Cat("Count Duku", 15)
cat3 = Cat("Dr Cat", 4)

def find_oldest_cat(*cats):
    oldest_cat = max(cats, key=lambda cat: cat.age)
    return oldest_cat

oldest_cat = find_oldest_cat(cat1, cat2, cat3)

print(f"The oldest cat is {oldest_cat.name}, and is {oldest_cat.age} years old.")


