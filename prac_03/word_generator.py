"""
CP1404/CP5632 - Practical
Random word generator - based on format of words

Another way to get just consonants would be to use string.ascii_lowercase
(all letters) and remove the vowels.
"""


def main():

    import random

    VOWELS = "aeiou"
    CONSONANTS = "bcdfghjklmnpqrstvwxyz"

    word_format = str(input("Input format: c for consonant, v for vowel"))
    word_format = word_format.lower()
    check = is_valid_format(word_format)

    while check is False:
        print("invalid format")
        word_format = str(input("Input format: c for consonant, v for vowel"))
        word_format = word_format.lower()
        check = is_valid_format(word_format)

    word = ""
    for kind in word_format:
        if kind == "c":
            word += random.choice(CONSONANTS)
        else:
            word += random.choice(VOWELS)
    print(word)


def is_valid_format(word_format):

    total = 0
    for char in word_format:
        if char == "c":
            total += 1
        elif char == "v":
            total += 1
    if total == len(word_format):
        return True
    else:
        return False

main()