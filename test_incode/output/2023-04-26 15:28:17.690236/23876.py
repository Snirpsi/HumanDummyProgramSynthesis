#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that removes user input. """    
    while True:
        command = input('Enter a command: ')
        if command == 'quit':
            break
        elif command == 'help':
            print('Available commands:')
            print('quit: Quit the program')
            print('help: Print this help')
        else:
            print('Invalid command')
