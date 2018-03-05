def main():
    name = get_name()
    frequency = get_frequency()
    sliced_str = slice_str(name, frequency)
    print (sliced_str)

def get_name():
    name = str(input("Enter your name"))
    return name

def get_frequency():
    frequency = int(input("How you would like it to be split"))
    return frequency

def slice_str(name, frequency):
    slice_str = name[::frequency]
    return slice_str


main()