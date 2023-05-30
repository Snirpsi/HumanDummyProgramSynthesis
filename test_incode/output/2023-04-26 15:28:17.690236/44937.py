#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that adds user input or opens user input. """    
    while True:
        command = input('Enter a command: ')
        if command == 'quit':
            break
        else:
            print('You entered', command)
