# Design a program that lets the user enter the total rainfall for each of 12 months into a list. The program should
# calculate and display the total rainfall for the year, the average monthly rainfall, and the months with the highest
# and lowest amounts.

import operator
# Creating an empty list
storage = []
# Creating a list to determine the month
months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December" ]
# This gets the user to input rainfal for the 12 months
for x in range(0, 12):

    user_input = int(input("Please enter The rainfall for this month: "))
    storage.append(user_input)
# This takes the list and finds the index location and the max rainfall, and assigns them to a value

month, max_rain = max(enumerate(storage), key=operator.itemgetter(1))

# this takes the list and finds the index location and the min rainfall, and assigns them to a value

Month, min_rain = min(enumerate(storage), key=operator.itemgetter(1))

# This adds the list together

total = sum(storage)

# this gets the average of the list
average = total / len(storage)
# Prints out the following information based on the output
print("The total rainfall for this year is:", total)
print("The average rainfall this year is: ", average)
print("The most rainfall this year is:", max_rain, "in the month of", months[month])
print("The least rainfall this year is:", min_rain, "in the month of", months[Month])





