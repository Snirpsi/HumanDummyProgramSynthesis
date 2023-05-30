#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that opens user input. """    
    while True:
        command = input('> ')
        if command == 'exit':
            break
        if command == 'help':
            print('\n'.join([
                'Commands:',
                '\texit: exit the program',
                '\thelp: print this help',
                '']))
        else:
            print('Unknown command: ' + command)
