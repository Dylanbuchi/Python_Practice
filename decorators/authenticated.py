# Create an @authenticated decorator
# that only allows the function to run
# if user1 has 'valid' set to True:


def authenticated(func):
    def temp(*args, **kwargs):
        if args[0]['valid']:
            print(f"Hello {args[0]['name']}")
        return func(*args, **kwargs)

    return temp


@authenticated
def message_friends(user):
    print('Your message has been sent with success')


if __name__ == "__main__":
    user1 = {
        'name': 'Homer',
        'valid': True
        #changing this will either
        #run or not run the message_friends function.
    }
    message_friends(user1)