
class Person:
    number_of_people = 0  # class attributes
    GRAVITY = -9.8

    def __init__(self, name):
        self.name = name
        #Person.number_of_people += 1
        Person.add_person()
        
    @classmethod
    def number_of_people_(cls):
        return cls.number_of_people

    @classmethod
    def add_person(cls):
        cls.number_of_people += 1

#Person.number_of_people = 8
p1 = Person("tim")
#print(Person.number_of_people)
p2 = Person('jill')
#print(Person.number_of_people)
print(Person.number_of_people_())