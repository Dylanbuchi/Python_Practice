def make_ubbi_dubbi(string: str):
    words = insert_ub_to(string)
    return ''.join(words)


def insert_ub_to(string: str):
    words = []
    for _, ch in enumerate(string):
        if ch in 'aeiou':
            words.append('ub')
        words.append(ch)
    return words


print(make_ubbi_dubbi('I love to drink coffee!'))