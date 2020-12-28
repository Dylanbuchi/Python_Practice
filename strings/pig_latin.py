def make_pig_latin(string: str):
    result = []
    for word in string.split():
        if word[0] in 'aeiou':
            result.append(f'{word}way')
        else:
            result.append(f'{word[1:]}{word[0]}ay')
    return ' '.join(result)


print(make_pig_latin('This sentence is in pig latin'))
