def get_age():
    age = 0
    while True:
        try:
            age = int(input("What's your age: "))
        except ValueError as error:
            print(f"Please enter a number\n{error}")
        else:
            break
    return age


def add(n, n2):
    result = 0
    try:
        result = n + n2
    except TypeError as error:
        print(f"Type Error\n{error}")
    return result


def main():
    my_age = get_age()
    add(2, 23)


if __name__ == "__main__":
    main()
    flag = False
    if not flag: raise Exception("The Flag is False")
