import collections
# User input
user_input = input("Please enter a sentence: ")
# changing input to lower case to make things easier to count
user_input = user_input.lower()
# These lines are to get rid of whitespaces and punctuation
user_input = user_input.replace(" ", "")

user_input = user_input.replace(",", "")

user_input = user_input.replace(".", "")

user_input = user_input.replace("'", "")

user_input = user_input.replace('"', "")
# Collections counter and getting the most common then printing it out for the user to read
print(collections.Counter(user_input).most_common(1)[0])
