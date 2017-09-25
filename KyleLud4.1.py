#Declare variables to be used in the while loop
stop = 0
calories = 4.2
minutes = 0
time = 0
#while loop with if statements to count the intervals, increments by 1 minute every iteration, when it hits an interval it will display the calories burned
while stop != 1:
    minutes = minutes + 1

    if minutes == 10:
        print ("The calories burned in " , minutes, "minutes are: ",  round(calories,2) * minutes)
    if minutes == 15:
        print ("The calories burned in ", minutes, "minutes are: ",   round(calories,2) * minutes)
    if minutes == 20:
        print ("The calories burned in ", minutes, "minutes are: ",   round(calories,2) * minutes)
    if minutes == 25:
        print ("The calories burned in ", minutes, "minutes are: ",   round(calories,2) * minutes)
    if minutes == 30:
        print ("The calories burned in ", minutes, "minutes are: ",   round(calories,2) * minutes)
        stop = 1 # stopping the program at 30 so it doesnt run infinitely


print(4.2 * 10)
