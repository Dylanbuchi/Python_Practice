import numpy


def trace(matrix: list) -> int:
    #calcualte the trace (diag)
    total = 0

    for i in range(len(matrix)):
        total += matrix[i][i]
    return total


def contruct_matrix(rows: int, colums: int) -> list:
    # construct a matrix
    matrix = []

    for row in range(rows):
        new_row = []
        for col in range(colums):
            new_row.append(row * col)
        matrix.append(new_row)
    return matrix


def display_matrix(matrix: list):
    # display the matrix
    print("--" * len(matrix) * 2)
    print(numpy.matrix(matrix))
    print("--" * len(matrix) * 2)


if __name__ == "__main__":

    matrix = contruct_matrix(5, 9)
    print(f"trace is: {trace(matrix)} \n")
    display_matrix(matrix)