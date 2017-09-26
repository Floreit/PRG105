

# get cost from user, pass to calc_cost
def main():
    structure_value = float(input("how much would it cost you to replace your home $ "))
    calc_cost(structure_value)

# calculate the cost o the insurance using the variable passed from the main as value


def calc_cost(value):
    insurance = value * .8
    print("You should get about: $ ", format(insurance, ".2f") , "For your home")


main()
