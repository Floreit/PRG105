

input = input("Please enter in numbers between 1-10 ")# taking input
#this if statement is taking the number, and responding with its corrosponding roman numeral sign
if input == '1':
    print("|")
elif input == '2':
    print("||")
elif input == '3':
    print("|||")
elif input == '4':
    print("|V")
elif input == '5':
    print("V")
elif input == '6':
    print("V|")
elif input == '7':
    print("V||")
elif input == '8':
    print("V|||")
elif input =='9':
    print("IX")
elif input == '10':
    print("X")
else:  #Error handling, in case someone enters any letters or numbers outside of the range this if statement handles
    print( str(input) , " Is not a valid entry, Please enter a number between 1-10")
