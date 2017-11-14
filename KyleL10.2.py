# class for questions
class Questions:
    question = " "
    answer1 = " "
    answer2 = " "
    answer3 = " "
    answer4 = " "
    correct_answer = " "
#initializer
    def __init__(self):
        question = " "
        answer1 = " "
        answer2 = " "
        answer3 = " "
        answer4 = " "
        correct_answer = " "
#all the functions to make the question for the trivia to be used later on
    def set_question(self, question):
        self.question = question

    def set_answer1(self, answer1):
        self.answer1 = answer1

    def set_answer2(self, answer2):
        self.answer2 = answer2

    def set_answer3(self, z):
        self.answer3 = z

    def set_answer4(self, a):
        self.answer4 = a

    def set_correct_answer(self, i):
        self.correct_answer = i
# Get question information to display them
    def get_question(self):
        return self.question

    def get_answer1(self):
        return self.answer1

    def get_answer2(self):
        return self.answer2

    def get_answer3(self):
        return self.answer3

    def get_answer4(self):
        return self.answer4

    def get_correct_answer(self):
        return self.correct_answer

# quickly declaring all the variables
q1 = Questions()
q2 = Questions()
q3 = Questions()
q4 = Questions()
q5 = Questions()
q6 = Questions()
q7 = Questions()
q8 = Questions()
q9 = Questions()
q10 = Questions()
# Question 1 to 10 down bellow
# -------------------------------------
q1.set_question("Who was the first president of the united states of america")
q1.set_answer1("Cleopatra")
q1.set_answer2("Will")
q1.set_answer3("Vader")
q1.set_answer4("Washington")
q1.set_correct_answer("Washington")

q2.set_question("Who won the 2016 predisential compaign?")
q2.set_answer1("Harambe")
q2.set_answer2("Hillary")
q2.set_answer3("Trump")
q2.set_answer4("Clinton")
q2.set_correct_answer("Trump")

q3.set_question("Who is the richest man in the world")
q3.set_answer1("Cleopatra")
q3.set_answer2("Trump")
q3.set_answer3("Jeff Bezos")
q3.set_answer4("Random Joe Blow")
q3.set_correct_answer("Jeff Bezos")

q4.set_question("What is the latest battlefield game")
q4.set_answer1("Call Of Duty WW")
q4.set_answer2("Battlefield 2")
q4.set_answer3("Lego Adventures")
q4.set_answer4("Battlefield 1")
q4.set_correct_answer("Battlefield 1")

q5.set_question("When did World War 2 end?")
q5.set_answer1("1945")
q5.set_answer2("1800")
q5.set_answer3("1946")
q5.set_answer4("1942")
q5.set_correct_answer("1945")

q6.set_question("When did world war 2 start")
q6.set_answer1("1945")
q6.set_answer2("1946")
q6.set_answer3("1938")
q6.set_answer4("1939")
q6.set_correct_answer("1939")

q7.set_question("When did World War 1 start")
q7.set_answer1("1914")
q7.set_answer2("1800")
q7.set_answer3("1918")
q7.set_answer4("1980")
q7.set_correct_answer("1914")

q8.set_question("When did World War 1 end")
q8.set_answer1("1800")
q8.set_answer2("1980")
q8.set_answer3("1918")
q8.set_answer4("1914")
q8.set_correct_answer("1918")

q9.set_question("Who Won league of legends worlds in 2016")
q9.set_answer1("TSM")
q9.set_answer2("Cloud9")
q9.set_answer3("CLG")
q9.set_answer4("SKT")
q9.set_correct_answer("SKT")

q10.set_question("Who won league of legends worlds in 2017")
q10.set_answer1("CLG")
q10.set_answer2("TSM")
q10.set_answer3("SSG")
q10.set_answer4("SKT")
q10.set_correct_answer("SSG")
# ------------------------------------------
# storing 5 questions into a list for each player
questions1 = [q1, q2, q3, q4, q5]
questions2 = [q6, q7, q8, q9, q10]
# declaring players and giving them a score of 0
player1 = 0
player2 = 0
# player 1 for loop to ask for all the questions
print("Player 1 turn")
for query in questions1:
    print("\n")
    print(query.get_question())
    print(query.get_answer1())
    print(query.get_answer2())
    print(query.get_answer3())
    print(query.get_answer4())
    guess = input("Please type the correct answer exactly as shown, mis-spelling/mis-capitalization will not be awarded points even if correct: ")
    if guess == query.get_correct_answer():
        print("Correct")
        player1 = player1 + 1

# player 2 for loop to ask for all the questions
print("Player 2 Turn")
for query in questions2:
    print("\n")
    print(query.get_question())
    print(query.get_answer1())
    print(query.get_answer2())
    print(query.get_answer3())
    print(query.get_answer4())
    guess = input("Please type the correct answer exactly as shown, mis-spelling/mis-capitalization will not be awarded points even if correct: ")
    if guess == query.get_correct_answer():
        print("Correct")
        player2 = player2 + 1
# comparing the scores between the 2 players
if player1 == player2:
    print("This round was a tie")
elif player1 > player2:
    print("Player 1 won")
else:
    print("Player 2 won")


print("Player 1 earned: ", player1, "Points")
print("Player 2 earned: ", player2, "Points")


