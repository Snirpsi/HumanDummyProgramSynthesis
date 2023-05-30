#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that prints user input. """    
    while True:
        command = input('> ')
        if command == 'exit':
            print('Bye!')
            break
        elif command == 'help':
            print('Commands:')
            print('  exit       Quits the program.')
            print('  help       Prints this help message.')
            print('  list       Prints a list of available commands.')
            print('  quit       Quits the program.')
        else:
            print('Unknown command: {}'.format(command))
