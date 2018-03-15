number_list = []
for n in range(0, 5):
    number = int(input("Enter a number: "))
    number_list.append(number)


print("The first number is {}".format(number_list[0]))
print("The last number is {}".format(number_list[-1]))
print("The smallest number is {}".format(min(number_list)))
print("The largest number is {}".format(max(number_list)))
print("The average of the numbers is {}".format(sum(number_list) / len(number_list)))