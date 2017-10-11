#1. Have a function that creates a list with 20 random integers between 1 and 100 (Assign them dynamically, store the list in a variable.)
#
#2. Have a function get a number from the user that is between 1 and 100 (validate to ensure a number (int or float) between 1 and 100 was entered
#instead of a string or something out of range).
#
#3. Pass both the list and the user's number to a function and have it display all numbers in the list that are greater than the user's number.
#If there are not any, display a message that explains there are no numbers in the list greater than the entered number.


import random


def randomly():
    list1 = []
    for x in range(0, 20):
        holding = random.randint(1, 100)
        list1.append(holding)

    return list1


def user_input():
    temp_input = []
    holding = 0
    for l in range(1, 20):
        holding = input("Please enter a number between 1 and 100")
        temp_input.append(holding)
        return user_input









randomly()
user_input()
xinput = user_input()
random = randomly()

for t in range(len(random)):
    print(random[t])

for m in range(len(xinput)):
    print(xinput[m])

