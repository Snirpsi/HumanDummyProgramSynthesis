#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that prints user input. """    
    while True:
        command = input('> ')
        if command == 'quit':
            break
        print('You entered', command)
        print('