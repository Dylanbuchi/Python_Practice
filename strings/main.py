def count_vowels(word: str) -> int:
    total = 0
    vowels = ['a', 'e', 'i', 'o', 'u']

    for i in word:
        if (i in vowels):
            total += 1
    return total


def demystify(l1_string: str) -> str:
    result = l1_string.replace("l", "a")
    result = result.replace("1", "b")
    return result


def main():

    print(demystify("lll111l1l1l1111lll"))
    print(demystify("111l1l11l11lll1lll1lll11111ll11l1ll1l111"))

    print(count_vowels("aaassseefffgggiiijjjoOOkkkuuuu"))
    print(count_vowels("aovvouOucvicIIOveeOIclOeuvvauouuvciOIsle"))


if __name__ == "__main__":
    main()