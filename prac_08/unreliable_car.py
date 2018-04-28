from prac_08.car import Car
import random


class UnreliableCar(Car):

    def __init__(self, name, fuel, reliability):
        """Initialise an UnreliableCar instance, based on parent class Car."""
        super().__init__(name, fuel)
        self.reliability = reliability

    def drive(self, distance):
        reliability_check = random.randint(0, 101)
        print (reliability_check)
        if reliability_check < self.reliability:
            distance = super().drive(distance)
            return distance
        else:
            distance = 0
            return distance
