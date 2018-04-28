from prac_07.guitar_classes import Guitar


def main():
    guitars = []
    guitars.append(Guitar("Gibson L-5 CES", 1922, "16035.40"))
    guitars.append(Guitar("Line 6 JTV-59", 2010, "1512.9"))
    name = input("Name: ")
    while name is not "":
        year = int(input("Year: "))
        cost = (input("Cost $"))
        guitars.append(Guitar(name, year, cost))
        print("{} ({}) : ${} added.".format(name, year, cost))
        name = input("Name: ")
    print("These are my guitars:")
    guitar_number = 0
    for guitar in guitars:
        guitar_number += 1
        print("Guitar {}:  {}".format(guitar_number, guitar))


main()