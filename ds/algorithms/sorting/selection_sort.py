def selection_sort(array: list):

    length = range(len(array) - 1)

    for i in length:
        i_min = i
        for j in range(i + 1, len(array)):
            if array[j] < array[i_min]:
                i_min = j
        if i_min != i:
            array[i_min], array[i] = array[i], array[i_min]


if __name__ == "__main__":
    array = [9, 8, 7, 0, 1]
    selection_sort(array)
    print(array)
