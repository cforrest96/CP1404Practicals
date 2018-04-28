from prac_08.silver_service_taxi import SilverServiceTaxi
from prac_08.taxi import Taxi


taxis = [Taxi(100, "Prius"), SilverServiceTaxi(100, "Limo", 2),
         SilverServiceTaxi(200, "Hummer", 4)]

total_cost = 0
taxi_selection = ""
menu_selection = input("Let's drive!\nq)uit, c)hoose taxi, d)rive\n>>>")
while menu_selection != "q":
    if menu_selection == "c":
        taxi_num = 0
        for taxi in taxis:
            print("{} - {}".format(taxi_num, taxi))
            taxi_num += 1
        select_taxi = int(input("Choose taxi\n>>>"))
        taxi_selection = taxis[select_taxi]
        print("Bill to date: ${:.2f}".format(total_cost))

    elif menu_selection == "d":
        distance = int(input("Drive how far?\n>>>"))
        try:
            taxi_selection.drive(distance)
            print("Your {} trip cost you ${:.2f}".format(taxi_selection.name, taxi_selection.get_fare()))
            total_cost += taxi_selection.get_fare()
            print("Bill to date ${:.2f}".format(total_cost))

        except AttributeError:
            print("Must select a taxi before driving")

    else:
        print("invalid menu selection")

    menu_selection = input("q)uit, c)hoose taxi, d)rive\n>>>")
print("Total trip cost: ${}".format(total_cost))
print("Taxis are now:")
for taxi in taxis:
    print(taxi)

