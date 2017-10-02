#fucntion that takes all the input then returns the value to be passed to yearly function
def monthly():
    loan = float(input("please enter your monthly loan payment: "))
    insurance = float(input("Please enter your monthly insurance payment: "))
    gas = float(input("Please enter your average monthly gas cost: "))
    maint = float(input("Please enter the average amount you spend on maintenance each month: "))
    monthly_cost = loan + gas + maint + insurance
    print("Your total monthly bill is : ", monthly_cost)
    return monthly_cost

#Function takes the monthly_cost from monthly function and multiplies it by 12, then prints it out.
def yearly(total):
    math = total
    math = round(math * 12, 3)

    print("Total cost of your car is: ", math)
    return math
#poor excuse for a main
monthly = monthly()
yearly(monthly)









