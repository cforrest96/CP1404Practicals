word_count = {}
string_to_count = str(input("Enter string"))
string_to_count = string_to_count.strip().split(" ")

for word in string_to_count:
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1
print(word_count)
word_list = sorted(word_count)
length_check = []
for word in word_list:
    length = len(word)
    length_check.append(length)


for word in word_list:
    print("{:{}} : {}".format(word, max(length_check) + 1, word_count[word]))