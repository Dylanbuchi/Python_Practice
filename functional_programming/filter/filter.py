def only_even(number):
    return number % 2 == 0


if __name__ == "__main__":

    my_list = [1, 2, 3, 4, 5, 6]
    evens = list(filter(only_even, my_list))

    print(f"filter list: {evens}")
    print(f"my list: {my_list}")