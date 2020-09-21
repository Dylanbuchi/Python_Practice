def binary_search(numbers, n):
    low = 0
    high = len(numbers) - 1

    while low <= high:
        i = (low + high) // 2
        mid = numbers[i]

        if mid == n:
            return i
        elif mid > n:
            high = i - 1
        else:
            low = i + 1


numbers = [i+1 for i in range(100)]

num = 23
index = binary_search(numbers, num)

if index is None:
    print("Number not found!")
else:
    print(f"Number {num} found at position {index}")
