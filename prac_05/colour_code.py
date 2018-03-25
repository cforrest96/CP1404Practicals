#function to search in database

COLOURS = {"AliceBlue": "#f0f8ff",
           "Antique White": "#faebd7",
           "beige": "#f5f5dc",
           "black": "#000000",
           "Blanched Almond": "#fffebcd",
           "BlueViolet": "#8a2be2",
           "brown": "#a52a2a",
           "burlywood": "#deb887",
           "CadetBlue": "#5f9ea0",
           "chocolate": "#d2691e"
           }

print(COLOURS)

colour_select = str(input("what colour do you want?"))
while colour_select != "":
    if colour_select in COLOURS:
        print("Hexadecimal colour code for {} is {}".format(colour_select, COLOURS[colour_select]))
    else:
        print("Not in database")
    colour_select = str(input("what colour do you want?"))
