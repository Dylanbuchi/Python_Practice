def get_grades(quantity):
    # get user grades and return as a list
    grades = []
    for i in range(1, quantity + 1):

        if i == 1:
            grade = int(input(f"What's your {i}st grade (0-100):\n"))
        else:
            grade = int(input(f"What's your {i}nd grade (0-100):\n"))
        grades.append(grade)
    return grades


def descending_order(grades):
    # sort grades inplace by descending order
    grades.sort(reverse=True)
    print(f"Your grades from highest to lowest are: {grades}")


def ascending_order(grades):
    # sort grades inplace ascending order
    grades.sort()


def remove_two_lowest_grades(grades):
    # drop 2 lowest grades
    grades.sort(reverse=True)
    for _ in range(2):
        print(f"removing grade {grades.pop(-1)}")


def get_highscore(grades):
    # get highest grade
    grades.sort(reverse=True)
    return grades[0]


def app():
    # main app
    grades = get_grades(4)
    print(f"Your grades are: {grades}")

    descending_order(grades)
    remove_two_lowest_grades(grades)

    print(f"Your remaining grades now are: {grades}")
    print(f"Your highest grade is a {get_highscore(grades)}!")


if __name__ == "__main__":
    app()