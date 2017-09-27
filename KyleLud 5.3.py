#function is to get the assesment value of the property
def assess_value(value):

    assessed_value = value * .6
    calc_tax(assessed_value)


#divide assessed_value by 100 and multiply it by .72 to get the final tax amount

def calc_tax(assessed_value):
    tax = (assessed_value / 100) * .72
    print("Your tax amount is $ ", format(tax, ',.2f'), sep=" ")



#main function will get base value and pass to assess_value
def main():
    base_value = float(input("What is the base value of your property $ "))
    assess_value(base_value)


main()
