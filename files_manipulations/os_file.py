import os
import datetime

file_name = "file.txt"


def main():
    # main method
    print(f"file exists: {file_exists}")
    print(f"file size: {file_size}")
    print(f"file absolute path: {abs_path}")
    print(f"file last modification: {file_datetime}")


# check if file exists
file_exists = os.path.exists(file_name)

# return size of the file
file_size = os.path.getsize(file_name)

# get the last modification time of the file
timestamp = os.path.getmtime(file_name)

# print time converted for readability
file_datetime = datetime.datetime.fromtimestamp(timestamp)

# get the absolute path of file
abs_path = os.path.abspath(file_name)

main()
