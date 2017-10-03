#Global variables and type  casting to a float early
calories = 0
calories = float(calories)

#takes input for the fat variable and multiplies it by 9 then sends it to the total calories globally
def fat():
    fat = float(input("How many grams of fat did you eat today?"))
    global calories
    fat = fat * 9
    calories = calories + fat
    print("you ate", fat, "calories from fat")

#Takes input for the carbs variable and multiplies it by 4, then sends it to the total calories globally
def carbs():
    carbs = float(input("How many carbs did you eat today?"))
    carbs = carbs * 4
    global calories
    calories = calories + carbs
    print("you ate", carbs, "calories from carbs")

#takes the input for protein variable and multiplies it by 4, then sends it to the total calories globally
def protein():
    protein = float(input("how many grams of protein did you eat today?"))
    protein = protein * 4
    global calories
    calories = calories + protein
    print("you ate", protein, "calories from protein")

#Who doesnt like a good main() function, also prints out the total calories and formats it to 2 decimal places
def main():
    print("Your total calories intake for today is: ", format(calories, '.2f'))
#This is where the magic begins with calling all those functions, including main
fat()
carbs()
protein()
main()
