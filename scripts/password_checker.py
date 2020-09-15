def password_checker(username, password):
    pass_len = len(password)
    converted_password = '*' * pass_len

    print(
        f"{username}, your password {converted_password} is {pass_len} letters long"
    )


def main():
    username = input("Username: ")
    password = input("Password: ")

    password_checker(username, password)


if __name__ == "__main__":
    main()
