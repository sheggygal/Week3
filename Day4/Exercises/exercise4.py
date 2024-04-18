class Family:
    def __init__(self, last_name, members):
        self.last_name = last_name
        self.members = members

    def born(self, **kwargs):
        self.members.append(kwargs)
        print("Congratulations to the", self.last_name, "family on the new addition!")

    def is_18(self, name):
        for member in self.members:
            if member['name'] == name:
                return member['age'] >= 18
        return False

    def family_presentation(self):
        print("Family Name:", self.last_name)
        print("Members:")
        for member in self.members:
            print("Name:", member['name'])
            print("Age:", member['age'])
            print("Gender:", member['gender'])
            print("Is Child:", member['is_child'])
            print()


members = [
    {'name': 'Mister', 'age': 35, 'gender': 'Male', 'is_child': False},
    {'name': 'Missis', 'age': 32, 'gender': 'Female', 'is_child': False}
]
family_instance = Family("Smith", members)

family_instance.born(name='Junior', age=0, gender='Male', is_child=True)


print("Is Mister over 18?", family_instance.is_18('Michael'))
print("Is Junior over 18?", family_instance.is_18('John'))

family_instance.family_presentation()
