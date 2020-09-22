import googletrans


def translate_in(lang, filename):
    with open(filename, 'r') as f:
        gt = googletrans.Translator()
        text = f.read()
        return gt.translate(text, lang).text


def append(filename, text):
    with open(filename, 'a', encoding="utf-8") as f:
        f.write("\n" + text)


if __name__ == "__main__":

    fname = r"files_manipulations\files\translate.txt"
    file_translated = r"files_manipulations\files\translated.txt"

    fr = translate_in('fr', fname)
    ko = translate_in('ko', fname)
    pt = translate_in('pt', fname)

    lst = [fr, ko, pt]

    for item in lst:
        append(file_translated, item)
