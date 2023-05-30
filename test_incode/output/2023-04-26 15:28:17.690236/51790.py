#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that returns user input. """    
    while True:
        choice = input('Choose an option: ')
        if choice == '1':
            print('You chose option 1')
        elif choice == '2':
            print('You chose option 2')
        else:
            print('Invalid input')
