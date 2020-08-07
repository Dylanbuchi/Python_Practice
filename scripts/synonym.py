import random
import sys


def print_menu(menu, word_to_synonym):
    # print the menu user interface
    print(menu)
    print_words(word_to_synonym)
    print()


def user_interface(word_to_synonym):
    # the user interface that takes a list of words to choose for getting synonyms
    menu = f"""
Choose a word from this list and I will give you a synonym!
Here are the words:
            """
    print_menu(menu, word_to_synonym)

    text = "What word would you like a synonym for: "
    user_word = ""

    while True:
        user_word = get_user_word(text)

        if user_word in word_to_synonym:
            print(
                f"a synonym for {user_word.title()} is {get_random_synonym(word_to_synonym, user_word)}"
            )
            break
        print("\nPlease enter a word from the list!")
        print_menu(menu, word_to_synonym)

    print(
        f"Would you like to see the others synonym for the word '{user_word.title()}' ? (y/n)"
    )
    response = input().lower().strip()

    if response == 'y':
        print()
        print_all_synonyms_from(user_word, word_to_synonym)
    sys.exit()


def get_user_word(text):
    # return word from user input
    return input(text).lower().strip()


def print_words(word_to_synonym: dict):
    # print the keys
    for word in word_to_synonym:
        print(f"- {word.title()}")


def get_random_synonym(word_to_synonym: dict, word: str):
    # return a random synonym from the given key
    synonyms = word_to_synonym[word]
    random.shuffle(synonyms)
    return synonyms[0].title()


def print_all_synonyms_from(word, word_to_synonym):
    # print every synonmy from the given word
    synonyms = word_to_synonym[word]
    print(f"'{word.title()}' synonyms are:")

    for synonym in synonyms:
        print(f"- {synonym.title()}")


def main():

    # list of synonyms
    hot_synonyms = ['balmy', 'summery', 'tropical', 'boiling', 'scorching']
    cold_synonyms = ['cool', 'chilly', 'freezing', 'frigid', 'polar']
    happy_synonyms = ['content', 'cherry', 'merry', 'jovial', 'jocular']
    sad_synonyms = ['unhappy', 'downcast', 'miserable', 'glum', 'melancholy']

    # dict key -> value
    word_to_synonym = {
        'hot': hot_synonyms,
        'happy': cold_synonyms,
        'cold': happy_synonyms,
        'sad': sad_synonyms,
    }

    # main app
    user_interface(word_to_synonym)


if __name__ == '__main__':
    main()