item_num = int(input("How many items do you have?"))
total_price = 0

while item_num < 0:
    print("Invalid Number of Items")
    item_num = int(input("How many items do you have?"))

for item in range(1, item_num + 1, 1):
    item_price = float(input("Price of Item {}: $".format(item)))
    total_price = total_price + item_price

if total_price > 100:
    total_price = total_price * 0.9
    print ("Total Price for {} items is ${}".format(item_num, total_price))

else:
    print("Total Price for {} items is ${}".format(item_num, total_price))

