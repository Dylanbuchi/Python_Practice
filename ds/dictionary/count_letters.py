def count_letters(word_list: list) -> (str, int):

    ALPHABET = "abcdefghijklmnopqrstuvwxyz"

    letter_count = {}

    for letter in ALPHABET:
        letter_count[letter] = 0

    for word in word_list:
        for letter in word:
            if letter in letter_count:
                letter_count[letter] += 1
    count = 0
    result_letter = ""

    for key, value in letter_count.items():
        if value > count:
            result_letter = key
            count = value
    return result_letter, count


if __name__ == "__main__":

    monty_quote = """listen strange women lying in ponds
    distributing swords is no basis for a system of government
    supreme executive power derives from a mandate from the masses 
    not from some farcical aquatic ceremony"""

    monty_words = monty_quote.split()
    letter, count = count_letters(monty_words)

    print(f"The letter '{letter}' appears the most. ({count}) times in total")