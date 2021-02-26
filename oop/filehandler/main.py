import os
import sys
sys.path.append("./oop")

from filehandler.names_file import NamesFile


def print_every_names_file_methods(names_file: NamesFile):
    print("\nLongest name:", names_file.get_longest_name())
    print("\nSum of every names length:",
          names_file.get_total_sum_of_names_length())
    print("\nAverage of every names length:",
          names_file.get_average_names_length())

    print("\nShortest names: ")
    names_file.print_shortest_names()


def create_every_file_from_names_file_methods(names_file: NamesFile):

    names_file.create_names_lengths_file(
        "oop/filehandler/output/names_lengths.txt")
    names_file.create_sorted_names_file(
        "oop/filehandler/output/sorted_names.txt")
    names_file.create_sorted_names_by_length_file(
        "oop/filehandler/output/sorted_names_by_length.txt")


def main():

    print(os.getcwd())
    names_file = NamesFile("oop/filehandler/data/names.txt")

    print_every_names_file_methods(names_file)
    create_every_file_from_names_file_methods(names_file)


if __name__ == "__main__":

    print(os.getcwd())
    main()