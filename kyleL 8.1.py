# input for user enterying there name
name = input('Type your name and press ENTER. ')
# split the input
name_list = name.split()


print(name_list)
# separate the initials
first = name_list[0][0]
second = name_list[1][0]
last = name_list[2][0]
# print out the initials for a user
print(first.title(),'.', second.title(),'.', last.title(), sep=" ")
