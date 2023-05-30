#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that enumerates user input or prints user input. """    
    while True:
        choice = input('Enter your choice: ')
        if choice == 'exit':
            print('Goodbye!')
            break
        else:
            print('You chose:', choice)
