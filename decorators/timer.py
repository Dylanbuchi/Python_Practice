from time import perf_counter
from functools import wraps


def timer(func):
    """timer decorator to time a function"""
    @wraps(func)
    def inner(*args, **kwargs):
        start = perf_counter()
        result = func(*args, **kwargs)
        end = perf_counter()

        time_elapsed = end - start

        args_list = [str(i)
                     for i in args] + [f"{k}={v}" for k, v in kwargs.items()]
        args_string = ', '.join(args_list)

        print(
            f"{func.__name__}({args_string}) took {time_elapsed:.6f}s to run")
        return result

    return inner


def calculate_recursive_fib(n):
    if n <= 2:
        return 1
    return calculate_recursive_fib(n - 1) + calculate_recursive_fib(n - 2)


@timer
def fib_iterative(n):
    fib_list = [1, 1, 2]
    if n == 0:
        return 1

    for i in range(3, n + 1):
        fib_list.append(fib_list[-2] + fib_list[-1])

    return fib_list[n - 1]


@timer
def fib_recursive(n):
    return calculate_recursive_fib(n)


def main():
    print(fib_recursive(35))
    print(fib_iterative(35))


if __name__ == "__main__":
    main()
