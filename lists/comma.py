def string_from(array: list) -> str:
    # transform a List into a String
    convert = [str(i) for i in array]
    convert.insert(-1, "and")
    string_before_last = ", ".join(convert[:-1])
    last_part = convert[-1]
    result = " ".join([string_before_last, last_part])
    return result


def main():

    array = ['apples', 'bananas', 'tofu', 'cats']
    array_2 = [1, 2, 3, 4, 5]
    array_3 = [1, 2, 'apples', 'bananas']

    examples = array, array_2, array_3

    for i in examples:
        print(string_from(i))


if __name__ == "__main__":
    main()