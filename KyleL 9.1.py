import os
import pickle
# Variables to be used with the if statement.
LOOK_UP = 1
ADD = 2
CHANGE = 3
DELETE = 4
QUIT = 5

# Who cant ever use a proper main

def main():
    emails = {}
    choice = 0
    if not os.path.exists('text.dat'):
        open('text.dat', 'w').close()


    while choice != QUIT:
        choice = get_menu_choice()
        if choice == LOOK_UP:
            look_up(emails)
        elif choice == ADD:
            add(emails)
        elif choice == CHANGE:
            change(emails)
        elif choice == DELETE:
            delete(emails)
        else:
            exit
# displays menu for the user to choose and uses while loop to keep things running

def get_menu_choice():

    print()
    print('Name and Email Address Catalog')
    print('------------------------------')
    print('1. Look up an email address')
    print('2. Add a new email address')
    print('3. Change an email address')
    print('4. Delete an email address')
    print('5. Quit the program')
    print()
    choice = int(input('Enter the choice: '))
    while choice < LOOK_UP or choice > QUIT:
        choice = int(input('Enter a valid choice: '))

    return choice

# checks to see what the mail address of the input name is

def look_up(emails):
    name = input('Enter a name: ')
    print(emails.get(name, 'Not found.'))
# lets users add name and email address to the program

def add(emails):

    name = input('Enter a name: ')
    address = input('Enter an email address: ')
    if name not in emails:
        emails[name] = address
        pickle.dump(emails, open('text.dat', "wb"))
    else:
        print('That entry already exists.')

# lets users change email address

def change(emails):
    name = input('Enter a name: ')
    if name in emails:
        address = input('Enter the new address: ')
        emails[name] = address

        pickle.dump(emails, open("text.dat", "w"))
    else:
        print('That name is not found.')

# lets users delete entries
def delete(emails):
    name = input('Enter a name: ')
    if name in emails:
        del emails[name]
    else:
        print('That name is not found.')


main()
