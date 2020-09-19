def multiply_by_2(number):
    return number * 2


def main():

    my_list = [1, 2, 3]
    map_list = list(map(multiply_by_2, my_list))

    print(f"map list: {map_list}")
    print(f"my list: {my_list}")


if __name__ == "__main__":
    main()
