#input, not much to say
x = input("Please enter a number between 1-7 depending on what you want: ")
#this if statement runs the numbers through and choses which day it is based upon what day of the week it is starting with sunday
if x == "1":
    print("Sunday")
elif x == "2":
    print("Monday")
elif x == "3":
    print("Tuesday")
elif x == "4":
    print("Wednesday")
elif x == "5":
    print("Thursday")
elif x == "6":
    print("Friday")
elif x == "7":
    print("Saturday")
else:# Troubleshoot,error handling/dumbing down so that people enter the correct number, no matter how badly they want to input the number 0
    print("Please enter a number between 1-7")
