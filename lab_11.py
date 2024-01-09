class Car:
    color = 'Red'
    def __init__(self, make, model):
        self.make = make
        self.model = model

car = Car("Toyota", "Supra")
car.year = 2022
print(car.color)
car.color = "Yellow"
print(car.color, car.year)
