class Human:
    def __init__(self, id_number, name, age, priority, blood_type):
        self.id_number = id_number
        self.name = name
        self.age = age
        self.priority = priority
        self.blood_type = blood_type
        self.family = []

    def add_family_member(self, person):
        self.family.append(person)
        person.family.append(self)


class Queue:
    def __init__(self):
        self.humans = []

    def add_person(self, person):
        if person.age > 60 or person.priority:
            self.humans = [person] + self.humans
        else:
            self.humans.append(person)

    def find_in_queue(self, person):
        for i in range(len(self.humans)):
            if self.humans[i].id_number == person.id_number:
                return i
        return -1

    def swap(self, person1, person2):
        index1 = self.find_in_queue(person1)
        index2 = self.find_in_queue(person2)
        if index1 != -1 and index2 != -1:
            self.humans[index1], self.humans[index2] = person2, person1

    def get_next(self):
        if self.humans:
            next_human = self.humans[0]
            self.humans = self.humans[1:]
            return next_human
        else:
            return None

    def get_next_blood_type(self, blood_type):
        for i in range(len(self.humans)):
            if self.humans[i].blood_type == blood_type:
                next_human = self.humans[i]
                self.humans = self.humans[:i] + self.humans[i+1:]
                return next_human
        return None

    def sort_by_age(self):
        priority_people = []
        older_people = []
        younger_people = []
        for person in self.humans:
            if person.priority:
                priority_people.append(person)
            elif person.age > 60:
                older_people.append(person)
            else:
                younger_people.append(person)
        sorted_queue = priority_people + older_people + younger_people
        next_human = self.get_next()
        self.humans = sorted_queue
        return next_human

    def rearrange_queue(self):
        rearranged_queue = []
        i = 0
        while i < len(self.humans):
            rearranged_queue.append(self.humans[i])
            if i < len(self.humans) - 1 and any(h in self.humans[i].family for h in self.humans[i + 1].family):
                i += 1
            i += 1
        self.humans = rearranged_queue


ana = Human("1", "Ana", 77, False, "A")
oleg = Human("2", "Oleg", 42, False, "O")
regina = Human("3", "Regina", 74, False, "AB")
lucy = Human("4", "Lucy", 35, False, "B")
dasha = Human("5", "Dasha", 1, True, "O")

# Add family members
ana.add_family_member(regina)
oleg.add_family_member(lucy)
ana.add_family_member(dasha)

# Create a Queue
queue = Queue()

# Add humans to the queue
queue.add_person(ana)
queue.add_person(oleg)
queue.add_person(regina)
queue.add_person(lucy)
queue.add_person(dasha)

# Test swapping
queue.swap(oleg, lucy)

# Test sorting
next_person = queue.sort_by_age()
print("Next person to be vaccinated:", next_person.name)

# Test rearranging queue
queue.rearrange_queue()

# Get next person in the rearranged queue
next_person = queue.get_next()
print("Next person in rearranged queue:", next_person.name)


