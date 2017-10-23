# Main function that will run everything
def main():
    # Setting numbers to the file and opening the file in read mode
    numbers = open('numbers.txt', 'r')
    count = 0
    total = 0
# For loop to add up and count the numbers inside numbers file, adds all values into one value
    for line in numbers:
        amount = float(line)
        total += amount
        count = count + 1
# getting the average of all the numbers in the file
    average = total / count
# print the total amount of numbers and the average of the numbers
    print("There were a total of: ", count, " numbers", sep="")
    print("The average of the numbers was: ", format(average, ',.2f'), sep="")
    numbers.close()
# Calling main function


main()
