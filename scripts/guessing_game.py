from random import randint
from sys import argv


def generate_random_numbers(start=1, end=100):
    return randint(start, end)


def get_user_number(n1=1, n2=100):
    number = 0
    while True:
        try:
            number = int(input(f"\nGuess a number from {n1} to {n2}: \n"))
            if number < n1 or number > n2:
                print(
                    f"\nOnly numbers between {n1} and {n2} (inclusive) are allowed\n"
                )
                continue
        except ValueError as error:
            print(f"Please enter a number only\nerror: {error}")
        else:
            break
    return number


def is_user_number_correct(user_num, correct_number):
    return user_num == correct_number


def game():
    n1 = int(argv[1])
    n2 = int(argv[2])
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
            print("\nOops, wrong answer, please try again")
            if user_number > random_number:
                print(f"\nthe correct number is less than {user_number}")
            else:
                print(f"\nthe correct number is greater than {user_number}")
            continue


def main():
    game()


if __name__ == "__main__":
    main()