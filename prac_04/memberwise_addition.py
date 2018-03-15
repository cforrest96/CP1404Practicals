def main():

    list_one = [1, 2, 3]
    list_two = [4, 5, 6]
    print(min(len(list_two), len(list_one)))
    memberwise_addition(list_one, list_two)


def memberwise_addition(list_one, list_two):

    output = []
    for i in range(max(len(list_one), len(list_two))):
        new_num = list_one[i] + list_two[i]
        output.append(new_num)
    print(output)

main()