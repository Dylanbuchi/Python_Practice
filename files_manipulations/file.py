file_name = "./files_manipulations/file.txt"


def write_file(file_name, line):
    # method to write into a file
    with open(file_name, "w") as file:
        for i in range(10):
            file.write(line)


def read_file(file_name):
    # method to read the file
    with open(file_name) as file:
        for line in file:
            print(line.strip())


def append_file(file_name, line):
    # method to append to file
    with open(file_name, "a") as file:
        file.write(line)


file = open(file_name)

def start():
    # main
    write_file(file_name, "From abc@email.com\n")
    append_file(file_name, "Hello")
    read_file(file_name)
    print(count_file(file_name))
    
    


def count_file(file_name):
    # count every line in file
    count = 0
    for line in file:
        count += 1
    return count

start()
file.close()

