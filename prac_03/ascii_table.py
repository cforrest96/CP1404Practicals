"""Get a number within a range from the user and reutnr the ascii alphabet equivalent"""

LOWER = 33
UPPER = 127


def main():

    number = get_number(LOWER, UPPER)
    while number not in range(LOWER, UPPER + 1):
        print("Invalid input")
        number = get_number(LOWER, UPPER)
    ascii_change = chr(number)
    print("The character for {} is {}".format(number, ascii_change))


def get_number(LOWER, UPPER):

    number_input = False
    while not number_input:
        try:
            number = int(input("Enter a number between {} and {}".format(LOWER, UPPER)))
            number_input = True
        except ValueError:
            print("Not an integer")

    return number


main()