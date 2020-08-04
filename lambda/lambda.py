import random


def get_line(array):
    # to print a line '-----' for visual purpose only
    return "\n" + "--" * 26


def to_string(array):
    # format a list into a string
    return " | ".join(map(str, array))


def get_result(array):
    # get the formated result
    return to_string(array) + get_line(array)


def print_result(dic):
    for k, v in dic.items():
        print(k, v)


def main():
    # list of nums (1-10) then randomly suffle the numbers
    nums = list(range(1, 11))
    random.shuffle(nums)

    # lambda for square nums
    square_nums = list(map(lambda num: num**2, nums))

    # filter only even numbers
    only_even_nums = list(filter(lambda num: num % 2 == 0, square_nums))

    # list of tuples from even list and square nums list
    list_tuples = list(
        map(lambda num1, num2: (num1, num2), only_even_nums, nums))

    # list of max nums from tuple list
    max_nums_list_tuples = list(
        map(lambda tup: max(tup[0], tup[1]), list_tuples))

    # dict with list name key and print result value
    listname_result = {
        "nums:": get_result(nums),
        "squares:": get_result(square_nums),
        "evens:": get_result(only_even_nums),
        "tuples:": get_result(list_tuples),
        "max num from tuples:": get_result(max_nums_list_tuples),
    }

    print_result(listname_result)


if __name__ == "__main__":
    print()
    main()
    print()