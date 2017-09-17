

#Info dump on user
print("Enter 1 for package a, 2 for package b, and 3 for package c: ")
print("Package A:	For $39.99 per month 450 minutes are provided. Additional minutes are $0.45 per minute.")
print("Package B:	For $59.99 per month 900 minutes are provided. Additional minutes are $0.40 per minute.")
print("Package C:	For $69.99 per month unlimited minutes provided.")
#taking input
package = input("Which package did you buy: ")
minutes = input("Enter how many minutes you have used: ")
# type casting to make things easier
minutes = int(minutes)
package = int(package)


#Package a, with some math to get the total bill, if they use more minutes than 450 it will sub those paid minutes and add the extra minutes to the bill.
if package == 1:
    print("You have Package a")
    if minutes > 450:

        math = minutes
        math = math - 450
        math = math * .45
        bill = 39.99 + math
        print("Your bill is $ " , bill)
#package b, same as package a, just with 900 minutes and different billing amount.
elif package == 2:
    print("You have Package b")
    if minutes > 900:
        math = minutes
        math = math - 900
        math = math * .40
        bill = 59.99 + math
        print("Your bill is $ " , bill)
    else:
        print("your Bill is $59.99")


#package c is the easiest as no math is required, since unlimited minutes, so it matters not how many minutes they have.
elif package == 3:
    print("You have Package c")
    print("Your Bill is $69.99")

else: #Error handling
    print("Please enter a package number between 1-3 for which package you have")






