"""Write a program asking how many "quick picks" to generate"""
import random

number_of_lines = int(input("How many lines would you like"))
dup_check = []
for n in range(1, number_of_lines + 1):
    pick = []
    for num in range(0, 6):
        number = random.randint(0, 45)
        while number in dup_check:
            number = random.randint(0, 45)
        dup_check.append(number)
        pick.append(number)
    pick.sort()
    pick = ", ".join(str(i) for i in pick)
    print(pick)