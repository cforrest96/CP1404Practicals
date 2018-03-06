"""
CP1404/CP5632 - Practical
Random word generator - based on format of words

Another way to get just consonants would be to use string.ascii_lowercase
(all letters) and remove the vowels.
"""
import random

VOWELS = "aeiou"
CONSONANTS = "bcdfghjklmnpqrstvwxyz"
MIN_LENGTH = 6
MAX_LENGTH = 20

rand_num = random.randint(MIN_LENGTH, MAX_LENGTH)
word_format = []
check = 0

while check < rand_num:
    choice = random.randint(0, 1)
    if choice == 0:
        letter = "v"
    else:
        letter = "c"
    word_format.append(letter)
    check += 1

word = ""
for kind in word_format:
    if kind == "c":
        word += random.choice(CONSONANTS)
    else:
        word += random.choice(VOWELS)

print(word)