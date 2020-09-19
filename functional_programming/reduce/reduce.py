from functools import reduce


def addition(my_list, index):
    return my_list + index


if __name__ == "__main__":
    my_list = [1, 2, 3, 4]
    reduced = reduce(addition, my_list)

    print(my_list)
    print(f"reduced: {reduced}")
