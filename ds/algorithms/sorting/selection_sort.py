def selection_sort(array: list):

    length = range(len(array) - 1)

    for i in length:
        i_min = i
        for j in range(i + 1, len(array)):
            if array[j] < array[i_min]:
                i_min = j
        if i_min != i:
            array[i_min], array[i] = array[i], array[i_min]


def find_smallest(array):
    small = array[0]
    small_index = 0
    for i in range(1, len(array)):
        if array[i] < small:
            small = array[i]
            small_index = i

    return small_index


def selection_sort_2(array):
    a = []
    for _ in range(len(array)):
        small = find_smallest(array)
        a.append(array.pop(small))
    return a


if __name__ == "__main__":
    array = [9, 8, 7, 0, 1]
    print(array)
    print("selection sort 2: ")
    print(selection_sort_2(array))
