import string

def count_letters(str):
    """Return the count of letters in str"""
    count = 0
    for char in str:
        if char.lower() in string.ascii_lowercase:
            count += 1
    return count