class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_name(self):
        return self.name

    def get_age(self):
        return self.age


if __name__ == "__main__":

    doggy = Dog("Dog", 2)
    print(doggy.get_name())
    print(doggy.get_age())