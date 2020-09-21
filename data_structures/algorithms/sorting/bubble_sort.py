def bubble_sort(array):
    # bubble sort algorithm
    is_sorted = False
    length = len(array) - 1

    while not is_sorted:
        is_sorted = True
        for i in range(length):
            if array[i] > array[i + 1]:
                swap(i, (i + 1), array)
                is_sorted = False


def swap(i, j, array):
    # helper method to swap values
    array[i], array[j] = array[j], array[i]


if __name__ == "__main__":

    array = [234, 9, 6, -12, 3, 0, 45, 1]

    print(f"\nList before bubble sort: {array}")
    print("------------------------------------------------------")

    bubble_sort(array)
    print(f"List after bubble sort: {array}")
