from pathlib import Path


def append_text(filename, text):
    with open(filename, 'a') as f:
        f.write(text + "\n")


if __name__ == "__main__":

    file_name = r"files_manipulations\files\test.txt"

    for i in range(5):
        append_text(file_name, "number: " + str(i))
