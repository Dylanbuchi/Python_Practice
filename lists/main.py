def string_from(array: list) -> str:
    # transform a List into a String
    convert = [str(i) for i in array]
    convert.insert(-1, "and")
    string_before_last = ", ".join(convert[:-1])
    last_part = convert[-1]
    result = " ".join([string_before_last, last_part])
    return result


# list of integers and returns the sum of those items \
# in the list that are not divisible by


def strange_sum(numbers: list) -> int:
    total = 0
    for i in numbers:
        if i % 3 == 0: continue
        total += i
    return total


def main():

    print(strange_sum([1, 2, 3, 4, 5, 1, 2, 3, 4, 5]))
    print(strange_sum(list(range(123)) + list(range(77))))

    array = ['apples', 'bananas', 'tofu', 'cats']
    array_2 = [3, 3, 3, 10, 15]
    array_3 = [1, 2, 'apples', 'bananas']

    print(f"strange sum: {strange_sum(array_2)}")

    examples = array, array_2, array_3

    for i in examples:
        print(string_from(i))


if __name__ == "__main__":
    main()