from exercise4 import Family
class TheIncredibles(Family):
    def use_power(self, name):
        for member in self.members:
            if member['name'] == name:
                if member['age'] >= 18:
                    print(f"{name}'s power: {member['power']}")
                else:
                    raise Exception(f"{name} is not over 18 years old and cannot use their power.")

    def incredible_presentation(self):
        print("*Here is our powerful family*")
        super().family_presentation()

incredibles_instance = TheIncredibles("Incredibles", [
    {'name': 'Michael', 'age': 35, 'gender': 'Male', 'is_child': False, 'power': 'fly', 'incredible_name': 'MikeFly'},
    {'name': 'Sarah', 'age': 32, 'gender': 'Female', 'is_child': False, 'power': 'read minds', 'incredible_name': 'SuperWoman'}
])

incredibles_instance.incredible_presentation()

incredibles_instance.born(name='Baby Jack', age=0, gender='Male', is_child=True, power='Unknown Power', incredible_name='BabyJack')

incredibles_instance.incredible_presentation()
