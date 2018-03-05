# Save name to file
nameFile = open("name.txt", "w")
userName = str(input("Enter your Name"))
nameFile.write(userName)
nameFile.close()

# Read name from file and print output
nameFile = open("name.txt", "r")
name = nameFile.read()
print ("Your name is {}".format(name))
nameFile.close()

numbers = open("numbers.txt", "r")
total = 0
number = numbers.read().split("\n")

total = 0
for n in number:
    n = int(n)
    total += n

print (total)