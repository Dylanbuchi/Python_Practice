def my_decorator(func):
    def box():
        print('-' * 10)
        print('|' + ' ' * 8 + '|')
        func()
        print('|' + ' ' * 8 + '|')
        print('-' * 10)

    return box


@my_decorator
def hello():
    print("hello")


if __name__ == "__main__":
    hello()
    hello_2 = my_decorator(hello)
    hello_2()