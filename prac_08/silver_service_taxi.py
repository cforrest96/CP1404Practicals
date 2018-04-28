from prac_08.taxi import Taxi


class SilverServiceTaxi(Taxi):
    flagfall = 4.50

    def __init__(self, name, fuel, fanciness):
        """Initialise a SilverServiceTaxi instance, based on parent class Taxi."""
        super().__init__(name, fuel)
        self.fanciness = float(fanciness)
        self.price_per_km = Taxi.price_per_km * self.fanciness

    def __str__(self):
        """Return a string like a Car but with current fare distance."""
        return "{}, plus flagfall of ${:.2f}".format(super().__str__(), self.flagfall)

    def get_fare(self):
        """Return the price for the taxi trip."""
        return super().get_fare() + self.flagfall



