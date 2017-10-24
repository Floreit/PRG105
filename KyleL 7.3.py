# opening the boys txt
boys_names = open('BoyNames.txt', 'r')
# opening the girls txt
girls_names = open('GirlNames.txt', 'r')
# creating the boys list
boys_list = []
# creating the girls list
girls_list = []
# doing a start of the readline and rstrip of both files
girls_record = girls_names.readline()
girls_record = girls_record.rstrip()
boys_record = boys_names.readline()
boys_record = boys_record.rstrip()
# ripping through all of girls file and adding it to girls list
while girls_record != "":

    girls_list.append(girls_record)
    girls_record = girls_names.readline()
    girls_record = girls_record.rstrip()
# ripping through all of the boys files and adding it to boys list
while boys_record != "":
    boys_list.append(boys_record)
    boys_record = boys_names.readline()
    boys_record = boys_record.rstrip()

# input for the user to input names, and stores them in a list, which is then checked in both lists to see if the names entered are in there
print("Enter the name of a boy, girl, or both, if you want to skip one simply press enter")
boys_name = input("please enter the name of a boy: ")
girls_name = input("Please enter the name of a girl: ")

# if statements determining if the entered names are among popular list
if girls_name in girls_list and boys_name in boys_list:
    print("Both names are popular names")
elif girls_name in girls_list:
    print("Your girls name is popular among girls")
elif boys_name in boys_list:
    print("Your boys name is popular among boys")
else:
    print("Your name is not among the popular names for either boys or girls")

# closing all files
boys_names.close()
girls_names.close()

