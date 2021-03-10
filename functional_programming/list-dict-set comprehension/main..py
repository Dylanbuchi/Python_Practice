from collections import Counter
from pprint import pprint


def main():
    # Lists comprehensions
    string = 'hello'

    ch_list = [ch for ch in string]
    print(f"{ch_list=}")

    numbers = [n for n in range(0, 10)]
    print(f"{numbers=}")

    square_numbers = [n**2 for n in range(0, 10)]
    print(f"{square_numbers=}")

    odd_numbers = [n for n in square_numbers if not n % 2 == 0]
    print(f"{odd_numbers=}")

    # Sets comprehensions
    my_set = {i for i in range(10)}
    my_set2 = {i for i in my_set if i > 5}

    print(f"{my_set=}")
    print(f"{my_set2=}")

    # Dictionaries comprehensions
    dict_test = dict(a=2, b=3, c=4)

    my_dict = {k: v**2 for k, v in dict_test.items()}
    dict_nums = {n: n * 2 for n in [1, 2, 3]}

    print(f"{my_dict=}")
    print(f"{dict_nums=}")

    # convert duplicates into a dict comprehension
    some_list = ['a', 'b', 'c', 'b', 'd', 'm', 'n', 'n']

    only_duplicates_letters = {
        k: v
        for k, v in Counter(some_list).items() if v >= 2
    }

    print(f"{only_duplicates_letters=}")

    # nested loops with lists comprehensions
    multiplication_table = [[i * j for j in range(1, 10 + 1)]
                            for i in range(1, 10 + 1)]

    print("\ntable: ", end="")
    pprint(multiplication_table)

    l1 = ['a', 'b', 'c', 'x']
    l2 = ['a', 'e', 'f', 'c']

    l3 = [''.join([i, j]) for i in l1 for j in l2 if i != j]

    print("\nletters: ")
    pprint(l3)

    to_zip1 = [1, 2, 3, 4, 5]
    to_zip2 = [10, 9, 8, 7, 6, 5, 4]

    zip_lists = [(i, j) for index_i, i in enumerate(to_zip1)
                 for index_j, j in enumerate(to_zip2) if index_i == index_j]

    print(zip_lists)


if __name__ == "__main__":
    main()
