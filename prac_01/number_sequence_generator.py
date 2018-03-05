menu_select = int(input("Choose a menu option by selecting the appropriate"
                        " number\n1. Show Odd Numbers\n2. Show Even Numbers\n"
                        "3. Show Squares\n4. Exit"))
num_one = int(input("Enter first number"))
num_two = int(input("Enter second number"))
check = num_two - num_one
if check < 0:
    print ("Second number must be larger than first number")
    menu_select = int(input("Choose a menu option by selecting the appropriate"
                            " number\n1. Show Odd Numbers\n2. Show Even Numbers\n"
                            "3. Show Squares\n4. Exit"))
    num_one = int(input("Enter first number"))
    num_two = int(input("Enter second number"))

while menu_select != 4:

    if menu_select == 1:

        if num_one % 2 == 0:

            for num in range (num_one + 1, num_two + 1, 2):
                print (num)

            menu_select = int(input("Choose a menu option by selecting the appropriate"
                                    " number\n1. Show Odd Numbers\n2. Show Even Numbers\n"
                                    "3. Show Squares\n4. Exit"))

            if menu_select != 4:
                num_one = int(input("Enter first number"))
                num_two = int(input("Enter second number"))

            else:
                pass

        else:
            for num in range (num_one, num_two + 1, 2):
                print (num)

            menu_select = int(input("Choose a menu option by selecting the appropriate"
                                    " number\n1. Show Odd Numbers\n2. Show Even Numbers\n"
                                    "3. Show Squares\n4. Exit"))

            if menu_select != 4:
                num_one = int(input("Enter first number"))
                num_two = int(input("Enter second number"))

            else:
                pass

    elif menu_select == 2:
        if num_one % 2 != 0:
            for num in range(num_one + 1, num_two + 1, 2):
                print(num)

            menu_select = int(input("Choose a menu option by selecting the appropriate"
                                    " number\n1. Show Odd Numbers\n2. Show Even Numbers\n"
                                    "3. Show Squares\n4. Exit"))

            if menu_select != 4:
                num_one = int(input("Enter first number"))
                num_two = int(input("Enter second number"))

            else:
                pass

        else:
            for num in range(num_one, num_two + 1, 2):
                print(num)

            menu_select = int(input("Choose a menu option by selecting the appropriate"
                                    " number\n1. Show Odd Numbers\n2. Show Even Numbers\n"
                                    "3. Show Squares\n4. Exit"))

            if menu_select != 4:
                num_one = int(input("Enter first number"))
                num_two = int(input("Enter second number"))

            else:
                pass

    else:
        for num in range(num_one, num_two + 1, 1):
            print (num * num)

        menu_select = int(input("Choose a menu option by selecting the appropriate"
                                " number\n1. Show Odd Numbers\n2. Show Even Numbers\n"
                                "3. Show Squares\n4. Exit"))

        if menu_select != 4:
            num_one = int(input("Enter first number"))
            num_two = int(input("Enter second number"))

        else:
            pass