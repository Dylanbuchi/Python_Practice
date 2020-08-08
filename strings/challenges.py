# Challenges are from www.w3resource.com


# helper methods
def print_questions_and_results(dic):
    # print questions with responses
    for k, v in dic.items():
        print(k, v)


def add_question(dic, question, result):
    # add question to the questions dict
    dic[question] = result


#--------------------------------------------
# results of questions in order from 1 to n


def get_len(string):
    #1
    # get length of the a string
    return f"string length is {len(string)}\n"


def get_character_to_number_occurence(string):
    #2
    # count the number of characters (character frequency) in a string

    temp = {}
    for ch in string:
        temp.setdefault(ch, 0)
        temp[ch] += 1
    return temp


def replace_with_dollar(string):
    #3
    #  Write a Python program to get a string from a given string
    # where all occurrences of its first char have been changed to '$',
    # except the first char itself

    first_letter = string[0]
    result = string[1:]
    result = result.replace(first_letter, '$')

    letters = list(result)
    letters.insert(0, first_letter)

    return "".join(letters)


def swap(string_1, string_2):
    #4
    # Write a Python program to get a single
    # string from two given strings,
    # separated by a space and swap the first two characters of each string

    result = f"{string_2} {string_1}"
    return result


def add_ing_or_ly(string):
    #5
    # Write a Python program to add 'ing' at the end of a given string (length should be at least 3).
    # If the given string already ends with 'ing' then add 'ly' instead.
    # If the string length of the given string is less than 3, leave it unchanged

    result = string
    str_ing = 'ing'
    str_ly = 'ly'

    if len(string) > 2:
        if string.endswith('ing'):
            result = string[:-3]
            result += str_ly
        else:
            result += str_ing
    return result


def longest_len(string):
    # 6
    # Write a Python function that takes a list of words and returns the length of the longest one
    words = string.split()
    longest = ''
    for word in words:
        if len(word) > len(longest):
            longest = word
    return f"longest word is : '{longest}'"


def remove_odd_index(string):
    # 7
    # Write a Python program to remove
    # the characters which have odd index values of a given string
    result = ''

    for i, ch in enumerate(string):
        if i % 2 == 0:
            result += ch
    return result


def add_tags(tag: str, string: str):
    # 8
    #Write a Python function to create the HTML string with tags around the word(s):
    open_tag = f"<{tag}>"
    close_tag = f"</{tag}>"

    result = ''.join([open_tag, string, close_tag])

    return result


def main():
    #key     ->    value
    question_to_response = {}

    #1
    add_question(
        question_to_response,
        "\n#1 Write a Pythonprogram to calculate the length of a string:\n",
        get_len(DEFAULT_STRING))
    #2
    add_question(
        question_to_response,
        "#2 Write a Python program to count the number of characters (character frequency) in a string:\n",
        get_character_to_number_occurence(DEFAULT_STRING))
    #3
    add_question(
        question_to_response,
        "\n#3 Write a Python program to get a string from a given string where all occurrences of its first char have been changed to '$', except the first char itself:\n",
        replace_with_dollar(DEFAULT_STRING))
    #4
    add_question(
        question_to_response,
        "\n#4 Write a Python program to get a single string from two given strings, separated by a space and swap the first two characters of each string:\n",
        swap(DEFAULT_STRING, DEFAULT_STRING_2))
    #5
    add_question(
        question_to_response,
        "\n#5 Write a Python program to add 'ing' at the end of a given string (length should be at least 3). If the given string already ends with 'ing' then add 'ly' instead. If the string length of the given string is less than 3, leave it unchanged:\n",
        add_ing_or_ly(DEFAULT_STRING))
    #6
    add_question(
        question_to_response,
        "\n #6 Write a Python function that takes a list of words and returns the length of the longest one:\n",
        longest_len(DEFAULT_STRING))
    #7
    add_question(
        question_to_response,
        "\n #7 Write a Python program to remove the characters which have odd index values of a given string:\n",
        remove_odd_index(DEFAULT_STRING))
    #8
    add_question(
        question_to_response,
        "\n #8 Write a Python function to create the HTML string with tags around the word(s):\n",
        add_tags('p', DEFAULT_STRING))

    print_questions_and_results(question_to_response)


if __name__ == "__main__":

    # default strings used for challenges
    DEFAULT_STRING = "welcome to String world!"
    DEFAULT_STRING_2 = "Good morning!"

    print(f"the string to be used will be : '{DEFAULT_STRING}':")

    main()