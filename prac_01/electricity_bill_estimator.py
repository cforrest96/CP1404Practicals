TARIFF_11 = 0.244618
TARIFF_31 = 0.136928


tariff = int(input("Which Tariff? 11 or 31"))
if tariff == 11:
    price = TARIFF_11
else:
    price = TARIFF_31
daily_use = float(input("Daily Use (KwH): "))
number_of_days = int(input("Number of days"))
bill_estimate = price * daily_use * number_of_days
print ("Estimated bill: ${}".format(bill_estimate))
