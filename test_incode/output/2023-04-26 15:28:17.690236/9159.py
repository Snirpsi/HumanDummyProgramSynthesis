#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that adds user input. """    
    while True:
        command = input('> ')
        if command == 'quit':
            break
        else:
            print('You typed', command, '