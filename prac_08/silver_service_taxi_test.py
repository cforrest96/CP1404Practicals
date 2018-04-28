from prac_08.silver_service_taxi import SilverServiceTaxi

silver_service_taxi = SilverServiceTaxi(200, "Hummer", 2)
print(silver_service_taxi)
silver_service_taxi.drive(18)
print(silver_service_taxi)

print(silver_service_taxi.get_fare())
test = float(silver_service_taxi.get_silver_fare())
print("{:.2f}".format(test))