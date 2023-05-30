#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that enumerates user input. """    
    while True:
        command = input('> ')
        if command == 'quit':
            break
        
        command = command.split()
        
        if len(command) == 1:
            print('Invalid command.')
            continue
        
        command = command[0]
        
        if command == 'help':
            print('Available commands:')
            print('\tquit')
            print('\thelp')
            print('\tlist')
            print('\tadd')
            print('\tremove')
            print('\tupdate')
            print('\tupdate-all')
            print('\tupdate-all