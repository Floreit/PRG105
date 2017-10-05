
def calc_average(first_test, second_test, third_test, fourth_test, fifth_test):

    score = (first_test + second_test + third_test + fourth_test + fifth_test) / 5
    return score

#takes the average and returns a letter grade
def determine_grade(average):

    if average <= 100 and average >= 90:
        grade = "A,"
    elif average <= 89 and average >= 80:
        grade = "B,"
    elif average <= 79 and average >= 70:
        grade = "C,"
    elif average <= 69 and average >= 60:
        grade = "D,"
    elif average < 60:
        grade = "F,"
    return grade
# Function asks for 5 scores, puts the input into calc_average function, then makes score equal to the result, pass score into determine_grade to get the letter grade
# Displays the results on the screen for the user


def main():

    first_test = int(input("What is the first score?"))
    second_test = int(input("What is the second score?"))
    third_test = int(input("What is the third score?"))
    fourth_test = int(input("What is the fourth score?"))
    fifth_test = int(input("What is the fifth score?"))
    score = calc_average(first_test, second_test, third_test, fourth_test, fifth_test)
    average_score = determine_grade(score)
    print("Your average score is:", average_score, " Which broken down is:" , score)



main()















