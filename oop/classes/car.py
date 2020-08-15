class Car:
    def __init__(self,
                 make='unknown',
                 model='unknown',
                 color='black',
                 year=2000,
                 price=10000.0):
        # constructor
        self._make = make
        self._model = model
        self._color = color
        self._year = year
        self._price = price

# ------- getters and setters -------

    @property
    def make(self):

        return self._make

    @make.setter
    def make(self, make):
        self._make = make

    @property
    def model(self):
        return self._model

    @model.setter
    def model(self, model):
        self._model = model

    @property
    def color(self):
        return self._color

    @color.setter
    def color(self, color):
        self._color = color

    @property
    def year(self):
        return self._year

    @year.setter
    def year(self, year):
        self._year = year

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, price):
        if price >= 0:
            if price == 0:
                print("This car is free!")
            self._price = price
        else:
            print("Error, Price is less than 0")


# ------- to string method -------

    def __str__(self):
        line = '---------------------'
        return f"""
{line}
Make:\t {self.make.title()}
Model:\t {self.model.title()}
Color:\t {self.color.title()}
Year:\t {self.year}
Price:\t {self.price}
{line}
"""


def main():
    # main method
    car = Car('buick', 'lesabre', 'red', 2000, 231)
    print(car)

    car.model = 'Batmobile'
    car.price = 0
    car.color = 'Black'

    print(car)

    # get cars from csv file and print them
    filename = r"files_manipulations\files\cars.csv"

    cars = []
    with open(filename) as csv_file:
        reader = csv_file.readlines()
        for data in reader[1:]:
            make, model, color, year, price = data.split(',')
            cars.append(Car(make, model, color, year, price))

    print(f"There are {len(cars)} cars:")

    for i, car in enumerate(cars):

        print(f"Car #{i+1}: {car}")


if __name__ == "__main__":
    main()
