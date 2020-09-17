class Cat:

    species = 'mammal'

    def __init__(self, name, age):
        self.name = name
        self.age = age


# 1 Create a function that finds the oldest cat
def get_oldest_cat_age(cats):
    return max(cats)


if __name__ == "__main__":

    # 2 Instantiate the Cat object with 3 cats
    tom = Cat('Tom', 7)
    jerry = Cat('Jerry', 5)
    tony = Cat('Tony', 2)

    cats_age = [tom.age, jerry.age, tony.age]

    # 3 Print out: "The oldest cat is x years old.".
    x = get_oldest_cat_age(cats_age)
    print(f"The oldest cat is {x} years old.")
