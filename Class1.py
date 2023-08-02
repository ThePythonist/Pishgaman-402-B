import time


class SedanCar:
    def __init__(self, hp, color, fuel, gb):
        self.horsepower = hp
        self.color = color
        self.fuel = fuel
        self.gearbox = gb
        self.rpm = 0

    def carbreak(self):
        print("Brrrrreak")

    def carhorn(self):
        print("Horrrrrn")

    def accelerate(self, value):
        for i in range(value):
            self.rpm += 1000
            time.sleep(3)
            print("Current round per motor is :", self.rpm)


samand = SedanCar("113", "white", "petrol", "manual")  # Instance ( Shey sakhtan )
dena = SedanCar("113", "black", "petrol", "automatic")  # Instance ( Shey sakhtan )

# dena.carbreak()
# samand.carhorn()
dena.accelerate(3)
