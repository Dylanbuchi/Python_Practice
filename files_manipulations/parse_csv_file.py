def parse_csv_file(file_name: str) -> list:
    # parse a csv file into a table
    table = []

    with open(file_name, "r") as csv_file:
        for line in csv_file:
            words = line.strip().split(",")
            table.append(words)
    return table


def print_table(table: list):

    for row in table:
        print(f"{row[0]:<20}", end="|")

        for col in row[1:]:
            print(f"{col:>3}", end="|")
        print()


if __name__ == "__main__":

    print()
    file_name = r"files_manipulations\files\hightemp.csv"
    table = parse_csv_file(file_name)
    print_table(table)
