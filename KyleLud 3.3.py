
#getting Age input, and type casting it to an int because FMTechnology
age = input("Please enter in your age")
age = int(age)
#determining what age you are, and a witty response for some of them
if age <= 1:
    print("You are an infant")
elif age > 1 and age < 13:
    print("You are a child, get over it")
elif age > 14 and age < 20:
    print("You are a teenage, lucky you")
elif age >= 20:
    print("You are an adult")
#else statement for error handling, trouble shooting shoddy coding, but also a use for the else statement.
else:
    print("Please enter a correct number")


