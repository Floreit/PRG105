# 1. Have a function that creates a list with 20 random integers between 1 and 100 (Assign them dynamically, store the list in a variable.)
#
# 2. Have a function get a number from the user that is between 1 and 100 (validate to ensure a number (int or float) between 1 and 100 was entered
# instead of a string or something out of range).
#
# 3. Pass both the list and the user's number to a function and have it display all numbers in the list that are greater than the user's number.
# If there are not any, display a message that explains there are no numbers in the list greater than the entered number.

#importing random to populate the list
import random

# Makes a list, fills it with 20 random numbers, then returns it
def randomly():
    list1 = []
    for x in range(0, 20):
        holding = random.randint(1, 100)
        list1.append(holding)

    return list1

# Asks the user for an input and verifies that its an actual number in between the asked sections
def user_input():
    holding = int(input("Please enter a number between 1 and 100: "))
    if holding >= 1 and holding <= 100:
        return holding
    else:
        print("please enter a valid number between 1 and 100")


# Main, activates the functions, then compares them and sorts the list and outputs the results for the user
def main():

    xinput = user_input()
    random2 = randomly()
    random2.sort()
    greater_than = [i for i in random2 if i >= xinput]
    print("The current list:", random2)
    print("User input is:", xinput)
    print("All numbers greater than the user input inside list:", greater_than)

# Running main function


main()
