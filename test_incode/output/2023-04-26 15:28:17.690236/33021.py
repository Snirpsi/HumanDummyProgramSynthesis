#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that prints user input. """    
    while True:
        command = input('Enter a command: ')
        if command == 'quit':
            print('Goodbye!')
            break
        elif command == 'help':
            print('Commands:')
            print('  quit: quit the program')
            print('  help: show this help')
            print('')
        else:
            print('Unknown command: {}'.format(command))

<|/ file filename=