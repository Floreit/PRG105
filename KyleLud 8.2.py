# dictonary to hold numbers to alphabet
phone_letters = {'A': '2', 'B': '2', 'C': '2', 'D': '3', 'E': '3',
                 'F': '3', 'G': '4', 'H': '4', 'I': '4', 'J': '5',
                 'K': '5', 'L': '5', 'M': '6', 'N': '6', 'O': '6',
                 'P': '7', 'Q': '7', 'R': '7', 'S': '7', 'T': '8',
                 'U': '8', 'V': '8', 'W': '9', 'X': '9', 'Y': '9',
                 'Z': '9'}

# input for the user
number = input('Enter an alpha-numeric phone number: ')
# holds the results of the scan bellow
result = []

# converts the letters to numbers
for x in number:
    if x.isdigit():
        str(result.append(x))
    if x.isalpha():
        value = phone_letters.get(x.capitalize())
        result.append(value)

# unique printing because reasons
print(result[0], result[1], result[2],"-", result[3], result[4], result[5], result[6],
      "-", result[7], result[8], result[9], sep="")
