try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))

    while denominator == 0:
        print("denominator cannot be zero")
        denominator = int(input("Enter the denominator: "))

    fraction = numerator / denominator
    print(fraction)

except ValueError:
    print("Numerator and denominator must be valid numbers!")

except ZeroDivisionError:
    print("Cannot divide by zero!")
    print("Finished.")

# Q1. ValueError will occur when numerator or denominator are not integers
# Q2. Zero Division Error will occur when denominator is equal to zero
# Q3. Yes