# Challenges are from www.w3resource.com


# helper methods
def print_questions_and_results(dic):
    for k, v in dic.items():
        print(k, v)


def add_question(dic, question, result):
    dic[question] = result


# results of questions in order from 1 to n
def get_len(string):
    #1 get length of the a string
    return f"string length is {len(string)}\n"


def get_character_to_number_occurence(string):
    # 2 count the number of characters (character frequency) in a string
    temp = {}
    for ch in string:
        temp.setdefault(ch, 0)
        temp[ch] += 1
    return temp


def replace_with_dollar(string):
    #4. Write a Python program to get a string from a given string
    # where all occurrences of its first char have been changed to '$',
    # except the first char itself
    first_letter = string[0]
    result = string[1:]
    result = result.replace(first_letter, '$')

    letters = list(result)
    letters.insert(0, first_letter)

    return "".join(letters)


def main():

    question_to_response = {}

    add_question(
        question_to_response,
        "\n#1 Write a Python program to calculate the length of a string:\n",
        get_len(DEFAULT_STRING))

    add_question(
        question_to_response,
        "#2 Write a Python program to count the number of characters (character frequency) in a string:\n",
        get_character_to_number_occurence(DEFAULT_STRING))

    add_question(
        question_to_response,
        "\n#4 Write a Python program to get a string from a given string where all occurrences of its first char have been changed to '$', except the first char itself:\n",
        replace_with_dollar(DEFAULT_STRING))

    print_questions_and_results(question_to_response)


if __name__ == "__main__":
    COUNT = 1

    DEFAULT_STRING = "welcome to String world!"

    print(f"the string to be used will be : '{DEFAULT_STRING}':")
    main()