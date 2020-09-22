import random

if __name__ == "__main__":
    print(__name__)
    print(random.randint(1, 100))
    print(random.choice([1, 2, 3]))

    lst = [1, 2, 3, 4, 5]

    random.shuffle(lst)
    print(lst)
