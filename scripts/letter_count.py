import sys


def greet(name):
    # greet
    print(f"Hello, {name}")


def get_letter_count_from(message, letter):
    # count occurences of a letter in a text
    return message.count(letter)


def app():

    name = input("What's your name ? \n").title().strip()
    greet(name)

    response = input(
        "I will count how many times a specific letter occurs in a messsage. Ready ?! \n"
    ).lower().strip()

    while response == "":
        response = input(
            "Please enter something or enter 'no' to quit:").lower().strip()
        if response == "no":
            print(f"Bye, {name}...")
            sys.exit()

    message = input("Please enter a message: \n").lower().strip()
    letter = input(
        "Wich letter would you like to count the occurrences of ? \n").lower(
        ).strip()

    letter_count = get_letter_count_from(message, letter)
    print(f"{name}, your message has {letter_count} '{letter}' in it.")


if __name__ == "__main__":
    app()
