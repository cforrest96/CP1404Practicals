name = str(input("What is your name?"))
menu_select = str(input("(H)ello\n(G)oodbye\n(Q)uit\n\n>>>"))
menu_select = menu_select.upper()

while menu_select != "Q":
    if menu_select == "H":
        print ("Hello {}".format(name))
        menu_select = str(input("(H)ello\n(G)oodbye\n(Q)uit\n\n>>>"))
        menu_select = menu_select.upper()

    elif menu_select == "G":
        print ("Goodbye {}".format(name))
        menu_select = str(input("(H)ello\n(G)oodbye\n(Q)uit\n\n>>>"))
        menu_select = menu_select.upper()

    else:
        print ("Invalid Choice")
        menu_select = str(input("(H)ello\n(G)oodbye\n(Q)uit\n\n>>>"))
        menu_select = menu_select.upper()

print("finished")