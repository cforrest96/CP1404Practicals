from prac_08.taxi import Taxi
from prac_08.unreliable_car import UnreliableCar

new_taxi = Taxi(100, "Prius 1")
new_taxi.drive(40)
print(new_taxi)
new_taxi.add_fuel(60)
new_taxi.start_fare()
new_taxi.drive(100)
print(new_taxi)
print(new_taxi.get_fare())
unreliable_taxi = UnreliableCar(100, "car", 50)
unreliable_taxi.drive(50)
print(unreliable_taxi)