def multiply_by_2(number):
    return number * 2


def main():
    my_list = [1, 2, 3]
    print(list(map(multiply_by_2, my_list)))
    print(my_list)


if __name__ == "__main__":
    main()
