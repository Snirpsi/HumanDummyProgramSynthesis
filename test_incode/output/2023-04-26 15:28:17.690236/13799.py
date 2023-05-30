#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that removes user input. """    
    while True:
        line = input('Enter a command: ')
        if line == 'quit':
            break
        elif line == 'help':
            print('Commands:')
            print('\tquit\tQuits the program.')
            print('\thelp\tDisplays this help message.')
        else:
            print('Unknown command.')
