#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that enumerates user input. """    
    while True:
        command = input('Enter a command: ')
        if command == 'quit':
            break
        elif command == 'help':
            print('Commands:')
            print('quit: quit program')
            print('help: print this message')
        else:
            print('Invalid command')
