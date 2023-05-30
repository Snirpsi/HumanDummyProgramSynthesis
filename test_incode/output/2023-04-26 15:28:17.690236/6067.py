#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that enumerates user input. """    
    while True:
        choice = input('Choose a number: ')
        if choice == 'quit':
            break
        else:
            print(choice)
