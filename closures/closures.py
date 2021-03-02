def counter():
    count = 0

    def increment_count():
        nonlocal count
        count += 1
        return count

    return increment_count


def add_amount(amount):
    def inner(n):
        return amount + n
    return inner


def print_counter():
    counter_1 = counter()
    counter_2 = counter()

    print(counter_1())
    print(counter_1())

    print(counter_2())
    print(counter_2())


def print_add_amount():
    add_5_to = add_amount(10)
    add_1_to = add_amount(1)

    print(add_5_to(2))
    print(add_1_to(10))


def main():
    print_counter()
    print_add_amount()


if __name__ == "__main__":
    main()