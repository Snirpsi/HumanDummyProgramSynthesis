#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that enumerates user input. """    
    while True:
        command = input('Enter a command: ')
        if command == 'quit':
            break
        elif command == 'help':
            print('Commands:')
            print('  quit: Quit the program.')
            print('  help: Display this help message.')
        else:
            print('Unknown command: ' + command)
