def my_generator(n):
    for i in range(1, n + 1):
        yield i**2


def generator_fib(n):
    a = 0
    b = 1
    lst = [a]

    for _ in range(n):
        temp = a
        a = b
        b = temp + b
        lst.append(a)
    return lst


if __name__ == "__main__":

    g = my_generator(5)

    for i in range(5):
        print(next(g))
    n = 8
    print(f"\nfib of {n}: {generator_fib(n)}")
