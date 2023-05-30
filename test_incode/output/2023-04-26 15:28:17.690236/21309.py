#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that enumerates user input. """    
    while True:
        command = input('Enter a command: ')
        if command == 'exit':
            break
        else:
            print('You entered', command)
