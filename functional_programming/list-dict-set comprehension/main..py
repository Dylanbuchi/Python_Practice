def main():
    # List comprehension
    string = 'hello'

    ch_list = [ch for ch in string]
    print(ch_list)

    numbers = [n for n in range(0, 10)]
    print(numbers)

    square_numbers = [n**2 for n in range(0, 10)]
    print(square_numbers)

    odd_numbers = [n for n in square_numbers if not n % 2 == 0]
    print(odd_numbers, "\n")

    # Set comprehension
    my_set = {i for i in range(10)}
    my_set2 = {i for i in my_set if i > 5}
    print(my_set)
    print(my_set2, "\n")

    #Dictionary comprehension
    dict_test = dict(a=2, b=3, c=4)

    my_dict = {k: v**2 for k, v in dict_test.items()}
    dict_nums = {n: n * 2 for n in [1, 2, 3]}
    print(my_dict)
    print(dict_nums)


if __name__ == "__main__":
    main()

    # convert duplicates into a list comprehension
    some_list = ['a', 'b', 'c', 'b', 'd', 'm', 'n', 'n']

    duplicates = []
    for value in some_list:
        if some_list.count(value) > 1:
            if value not in duplicates:
                duplicates.append(value)
    print(duplicates)

    converted_list = list({ch for ch in some_list if some_list.count(ch) > 1})
    print(converted_list)
