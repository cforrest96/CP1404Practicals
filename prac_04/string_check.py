user_input = str(input("Enter a string"))
string_list = []
dupe_list = []
while user_input is not "":
    if user_input not in dupe_list and user_input in string_list:
        dupe_list.append(user_input)
    string_list.append(user_input)
    user_input = str(input("Enter a string"))

dupe_list = ", ".join(dupe_list)
print("Strings repeated: {}".format(dupe_list))


