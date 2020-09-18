class Pets():
    def __init__(self, animals):
        self.animals = animals

    def walk(self):
        for animal in self.animals:
            print(animal.walk())


class Cat():
    is_lazy = True

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def walk(self):
        return f'{self.name} is just walking around'


class Simon(Cat):
    def sing(self, sounds):
        return f'Simon: {sounds}'


class Sally(Cat):
    def sing(self, sounds):
        return f'Sally: {sounds}'


#1 Add another Cat
class Tom(Cat):
    def sing(self, sounds):
        return f'Tom: {sounds}'


#2 Create a list of all of the pets (create 3 cat instances from the above)
simon = Simon('Simon', 7)
sally = Sally('Sally', 3)
tom = Tom('Tom', 4)

my_cats = [simon, sally, tom]

for cat in my_cats:
    print(cat.sing("miaw"))

#3 Instantiate the Pet class with all your cats use variable my_pets
my_pets = Pets(my_cats)

#4 Output all of the cats walking using the my_pets instance
my_pets.walk()
