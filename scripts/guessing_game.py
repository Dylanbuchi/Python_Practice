from random import randint


def generate_random_numbers(start, end):
    return randint(start, end)


def get_user_number(n1, n2):
    number = 0
    while True:
        try:
            number = int(input(f"Guess a number from {n1} to {n2}:"))
            if number < n1 or number > n2:
                print(
                    f"Only numbers between {n1} and {n2} (inclusive) are allowed"
                )
                continue
        except ValueError as error:
            print(f"Please enter a number only, {error}")
        else:
            break
    return number


def is_user_number_correct(user_num, correct_number):
    return user_num == correct_number


def game():
    n1 = 1
    n2 = 100
    random_number = generate_random_numbers(n1, n2)

    while True:
        user_number = get_user_number(n1, n2)
        user_is_correct = is_user_number_correct(user_number, random_number)

        if user_is_correct:
            print(
                f"Congratulations, you guessed right! The number was {random_number}"
            )
            break
        else:
            print("Oops, wrong answer, please try again")
            if user_number > random_number:
                print(f"the correct number is less than {user_number}")
            else:
                print(f"the correct number is greater than {user_number}")
            continue


def main():
    game()


if __name__ == "__main__":
    main()