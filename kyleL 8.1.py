name = input('Type your name and press ENTER. ')
name_list = name.split()

print(name_list)

first = name_list[0][0]
second = name_list[1][0]
last = name_list[2][0]

print(first.title(),'.', second.title(),'.', last.title(), sep=" ")
