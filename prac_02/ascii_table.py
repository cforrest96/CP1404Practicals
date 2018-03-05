LOWER = 33
UPPER = 127

letter = str(input("Enter a character"))
ascii_change = ord(letter)
print("The ASCII code for {} is {}".format(letter, ascii_change))

number = int(input("Enter a number between 33 and 127"))
while number not in range(LOWER, UPPER + 1):
    print("invalid input")
    number = int(input("Enter a number between 33 and 127"))
ascii_change = chr(number)
print("The character for {} is {}".format(number, ascii_change))

for number in range(LOWER, UPPER + 1):
    ascii = chr(number)
    print("{:3}{:>3}".format(number, ascii))