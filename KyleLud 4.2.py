days = int(input("How many days will you work for pennies a day?"))

print("Days Worked    |  Amount  Earned  That  Day")
print("------------------------------------------")
count = 1

pay = 0.01

str = "     |"
# 3 spaces for number 10 spaces for |
while count <= days:


    day = count
    print("   ",f'{day:>5}' , str , "$ " , f'{pay:.2f}' )


    pay = pay + pay


    count = count + 1

print(" ")
print("Total pay is: " , pay)

