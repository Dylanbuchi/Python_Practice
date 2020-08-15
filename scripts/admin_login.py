import sys
import getpass


def user_interface():
    # user interface interaction
    username = get_username()
    user_to_password.setdefault(username, 0)

    while True:
        password = get_password()
        if user_to_password[username] == 0:
            break
        if check_user_password(
                username,
                password) == False and user_to_password[username] != 0:
            print("wrong password")
            continue
        break

    if is_new_user(username):
        print(f"Welcome {username}, you are now logged in!")

    else:
        print(f"Welcome back {username}")

    add_user(username, password)

    # admin
    if is_admin(username):
        print("The current user database: ")
        for user, password in user_to_password.items():
            print(f"Username: {user}, Password: {password}")
    # normal users
    else:
        response = input("press '1' to change your password or '0' to exit: ")

        if response == '0':
            sys. ()
        elif response == '1':
            change_password()


def change_password():
    # change user's password
    password = ''
    confirm_password = ''

    while len(password) < 8:
        password = getpass.getpass("Enter your new password:")

    while (password != confirm_password):
        confirm_password = getpass.getpass("Confirm your new password: ")

    print("password changed with success!")


def check_user_password(user, password):
    # check if user is entering his correct password
    user_password = user_to_password[user]

    return user_password == password


def is_admin(user):
    # return true if user is an admin
    return user == 'admin'


def is_new_user(user):
    # return true if user is a new one
    return user_to_password[user] == 0


def add_user(user, password):
    # add user to the dict of user to password
    if user_to_password[user] == 0:
        user_to_password[user] = password


def prompt_for_password():
    # ask user to enter a valid password
    password_invalid = True
    while password_invalid:

        password = get_password()
        if is_valid_password(password):
            password_invalid = False
    return password


def get_password():
    # get user's password
    return getpass.getpass("Enter your password: ")


def get_username():
    # get user's username
    return input("Enter your username: ")


def is_valid_password(password):
    # return true if the password is valid
    if len(password) < 8:
        return False
    else:
        return True


def app():
    # main app

    user_interface()


if __name__ == '__main__':

    user_to_password = {
        'admin': '12345678',
        'johny4': 'johnn',
        'bobby34': 'hahaha',
        'helmet23': 'password',
        'doudou': 'hello21',
    }

    app()