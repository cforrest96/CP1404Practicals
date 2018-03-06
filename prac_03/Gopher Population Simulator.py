"""Track population of Gophers near library"""

import random

POPULATION = 1000
PERIOD = 10
POP_INCREASE_LOWER = 10
POP_INCREASE_UPPER = 20
POP_DECREASE_LOWER = 5
POP_DECREASE_UPPER = 25

def main():

    starting_point = 0
    new_population = POPULATION
    print("Welcome to the Gopher Population Simulator!")

    while starting_point < PERIOD:

        born_pop_percent = get_percentage(POP_INCREASE_LOWER, POP_INCREASE_UPPER)
        born_pop = born_pop_percent * new_population
        born_pop = int(born_pop)

        dead_pop_percent = get_percentage(POP_DECREASE_LOWER, POP_DECREASE_UPPER)
        dead_pop = dead_pop_percent * new_population
        dead_pop = int(dead_pop)

        new_population = new_population + born_pop - dead_pop
        starting_point += 1

        print("Year {}\n*****\n{} gophers were born. {} died.\n"
              "Population: {}\n".format(starting_point, born_pop,
                                      dead_pop, new_population))


def get_percentage(lower, upper):
    percentage = random.randint(lower, upper)
    percentage = float(percentage) / 100
    return percentage

main()