
#declaring all variables to be used in the while loop, as well as input for the first while loop
years = int(input("Please enter in the number of years"))
yearsCount = 0
totalRainYears = 0
EndMonthRain = 0
totalRain = 0
while yearsCount < years:
    monthsCount = 0

    EndMonthRain = 0
    monthsCount = 0
    # print("totalRainYears = ", totalRainYears)
    # print("yearcount = ", yearsCount)
    while monthsCount < 12:
        rain = input("Please enter in the number of inches of rainfall this month")
        rain = int(rain)
        monthsCount = monthsCount + 1
        totalRain = totalRain + rain
        print("totalrain = ", totalRain, "monthsCount = ", monthsCount)
        if monthsCount == 12:
            EndMonthRain = totalRain
            totalRainYears = EndMonthRain + totalRainYears
            yearsCount = yearsCount + 1
            print(" End of Year ")
        elif yearsCount == years:
            print("you messed up") #harsh reminder and error handling

N = yearsCount * 12
average = totalRainYears / N
average = round(average,2)

# print("Yearcount = ", yearsCount) # Testing purposes
print("Total number of months = ", N)
print("TotalRainfall = ", totalRainYears)
print("The Average Rainfall Per Month", average)
