import os

# create folder
os.mkdir("hehe")

# remove fodler
os.rmdir("hehe")

# rename folder or file
os.rename("a", "b")
os.rename("b", "a")


def get_current_path():
    # get current working path
    current_directory = os.getcwd()

    print(current_directory)
    return current_directory

get_current_path()

# list items in selected directory
print(os.listdir("a"))

dir = "a"

#check if there is files or fodlers
for name in os.listdir(dir):
    
    fullname = os.path.join(dir, name)
    
    if os.path.isdir(fullname):
        print(f"{fullname} is a directory")
    else:
        print(f"{fullname} is a file")    
   

