import random


def create_random_list():
    nums = []
    for i in range(4):
        nums.append(random.randint(1, 10))
    return nums


if __name__ == "__main__":
    list_1 = create_random_list()
    list_2 = create_random_list()
    list_3 = create_random_list()

    print(list_1, list_2, list_3)
    zipped = list(zip(list_1, list_2, list_3))
    print(f"zipped: {zipped}")
