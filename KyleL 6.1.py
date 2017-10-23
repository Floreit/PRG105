# Main function that will run everything
def main():
    # Setting names to the file and opening the file in read mode
    names = open('names.txt', 'r')
    count = 0
    # set first line of record and rstrip before while loop
    record = names.readline()
    record = record.rstrip()
# while loop to parse through the file read the line then continue down the line
    while record != "":
        print(record)
        record = names.readline()
        record = record.rstrip()
        count = count + 1
    names.close()
    print("There are ", count, " names in this file", sep="" )
# Calling main function
main()
