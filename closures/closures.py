def counter():
    count = 0

    def increment_count():
        nonlocal count
        count += 1
        return count

    return increment_count


def main():
    counter_1 = counter()
    counter_2 = counter()

    print(counter_1())
    print(counter_1())
    
    print(counter_2())
    print(counter_2())


if __name__ == "__main__":
    main()