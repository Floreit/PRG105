#delcaring variables and input
days = int(input("How many days will you work for pennies a day?"))

print("Days Worked    |  Amount  Earned  That  Day")
print("------------------------------------------")
count = 1

pay = 0.01
#useless but kept it due to experimentation and not wanting to break things
str = "     |"
# 3 spaces for number 10 spaces for |
while count <= days:


    day = count
    #           This thing here, is called formatting, keeps the numbers going left and aligned perfectly
    print("   ",f'{day:>5}' , str , "$ " , f'{pay:.2f}' )


    pay = pay + pay


    count = count + 1 #stops the loop when reaching input days

print(" ")
print("Total pay is: " , pay)

