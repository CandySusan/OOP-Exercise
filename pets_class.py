class Pets:

    all = "mammals"

    def __init__(self, age, name, number):
        self.name = name
        self.age = age
        self.number = number


# instance1 = Pets("age", "name", "number")
# instance1 = Pets("age", "name", "number")
# instance1 = Pets("age", "name", "number")
Dog = Pets(12, "Pry", 3)
Tom = Pets(6, "Tom", 3)
Fletcher = Pets(6, "Fletcher", 3)
Larry = Pets(9, "Larry", 3,)

print(f"I have {Dog.number} dogs")
print(f"{Tom.name} is {Tom.age}")
print(f"{Fletcher.name} is {Fletcher.age}")
print(f"{Larry.name} is {Larry.age}")
print(f"And they are all {Pets.all}. Ofcourse")


class Dog:
    is_hungry = True

    def __init__(self, is_hungry, walk):
        self.is_hungry = is_hungry
        self. walk = walk


Tom = Dog("not hungry", True)
print(f"All my dogs are {Tom.is_hungry}")


def eat(self):
    pass
