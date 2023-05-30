#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that returns user input. """    
    while True:
        choice = input('\nEnter your choice: ')
        if choice == 'quit':
            print('Goodbye!')
            break
        else:
            print('Invalid input')
