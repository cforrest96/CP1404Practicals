"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""
def main():

    score = float(input("Enter score: "))
    while score < 0 or score > 100:
        print("Invalid Score")
        score = float(input("Enter score: "))

    result = check_score(score)
    print (result)

def check_score(score):

    if score < 50:
        result = "Bad Score"
        return result

    elif score < 90:
        result = "Passable"
        return result

    else:
        result = "Excellent!!!"
        return result


main()
