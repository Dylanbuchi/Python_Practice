import re


def search_pattern(regex, string, specialcase=re.UNICODE):
    # search pattern regex in the string, optional arg unicode by default
    result = re.search(regex, string, specialcase)
    return result


def regex_examples():

    # the r is for a raw string
    # the . matches any characters and
    print(search_pattern(r"l.l", "lol"))

    # use [] to specify a range
    print(search_pattern(r"[0-9]", "abcd2"))

    # [range of lower letter and upper letter]
    print(search_pattern(r"[Jj]ava", "java"))
    print(search_pattern(r"[pP]ython", "Python"))

    # ignore upper lower cases
    print(search_pattern(r".eans", "Jeans", re.IGNORECASE))

    # (the | is or) to match the first a or b
    print(search_pattern(r"cat|dog", "there is a cat"))

    # (* qualifier) is used for infinite number of characters or 0
    print(search_pattern(r"py[a-z]*n", "pytttttthhhhhhoooooooon"))
    print(search_pattern(r"numbers:[0-9]..*", "numbers:01234567.."))

    # (+ qualifier) for 1 or more characters
    print(search_pattern(r"a+h!", "aaaaaaah!"))
    print(search_pattern(r"l+o+l+!", "lllooooooolllll!"))

    # (the ^ is used to match on the start of the line!)
    print(search_pattern(r"^start", "start, end!"))

    # (the $ is used to match on the end of the line!)
    print(search_pattern(r"end$", "start, end"))

    # (the ? is used to match the character before it 0 or 1 time)
    print(search_pattern(r"j?ava", "lava"))
    print(search_pattern(r"j?ava", "java"))

    # the \ is to escape a character
    print(search_pattern(r"\.com", "google.com"))

    # \w is used to match any alphabet, numeric, and underscores _ characters only
    print(search_pattern(r"\w*", "abc089__hehe"))

    # \d is used to match any digits characters only
    print(search_pattern(r"\d*", "123"))

    # \s is used to match white spaces characters only
    print(search_pattern(r"\shey*", " hey"))


def practice():

    pattern = r"^[a-zA-Z\s]*[0-9]*$"

    print(search_pattern(pattern, "this is valid"))
    print(search_pattern(pattern, "this is valid 34"))
    print(search_pattern(pattern, "ThisIsValid"))
    print(search_pattern(pattern, "  ThisIsValid  "))

    time = r"(1[012]|[0-9]):(0[0]|[01-59]+) ?([amAM]+|[pmPM]+)"
    print(search_pattern(time, "12:00 AM"))

    pattern = r"^[\w \. \- \+]+\.[a-zA-Z]+$"
    print(search_pattern(pattern, "gmail.com"))

    pattern = r"\([a-z A-Z]+\)|\([\w]+\)"
    result = re.search(pattern, "hello (IG)")
    print(result)

    pattern = r"^[\w \s]+[\s]{1,}[0-9]{5}|[0-9]{5}-[0-9]{4}"
    result = re.search(
        pattern, "Their address is: 123 Main Street, Anytown, AZ 85258-0001.")
    print(result)


def main():

    print("Practice: ")
    practice()

    print("Examples: ")
    regex_examples()


main()
