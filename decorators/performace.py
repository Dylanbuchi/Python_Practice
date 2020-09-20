import time


def performance(func):
    def temp(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)

        end = time.time()
        seconds = round((end - start), 2)

        print(f"This function took {seconds} seconds to run")
        return result

    return temp


@performance
def test():
    for i in range(3434):
        i * 2
        for i in range(3430):
            i += 1


if __name__ == "__main__":
    test()