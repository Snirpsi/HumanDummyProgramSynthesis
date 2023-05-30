#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that returns user input. """    
    while True:
        command = input('Enter a command: ')
        if command == 'quit':
            print('Goodbye!')
            break
        else:
            print('You entered: ' + command)
            