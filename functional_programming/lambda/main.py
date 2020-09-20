if __name__ == "__main__":

    # square
    my_list = [3, 4, 5]

    square_list = list(map(lambda item: item**2, my_list))

    print(square_list)

    #sorting list by second tuple item
    list_tuples = [(0, 2), (4, 3), (9, 9), (10, -1)]

    list_tuples.sort(key=lambda t: t[1])
    print(list_tuples)
