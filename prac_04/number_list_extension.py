number_list = []
total = 1
number = int(input("Number {}: ".format(total)))
while number >= 0:
    number_list.append(number)
    total += 1
    number = int(input("Number {}: ".format(total)))

print("The first number is {}".format(number_list[0]))
print("The last number is {}".format(number_list[-1]))
print("The smallest number is {}".format(min(number_list)))
print("The largest number is {}".format(max(number_list)))
print("The average of the numbers is {}".format(sum(number_list) / len(number_list)))