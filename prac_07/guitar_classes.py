class Guitar:
    def __init__(self, name="", year=0, cost=""):
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        return "{:>20} ({}), worth ${:10} {}".format(self.name, self.year, self.cost, "(vintage)" if
                                                    self.is_vintage(2018) else "")

    def get_age(self, current_year):
        guitar_age = current_year - self.year
        return guitar_age

    def is_vintage(self, current_year):
        if self.get_age(current_year) >= 50:
            return True
        else:
            return False
