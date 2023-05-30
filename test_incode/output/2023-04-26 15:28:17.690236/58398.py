#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that iterates over user input and adds a port. """    
    port = 'COM1'
    
    while True:
        line = input('Enter a command: ')
        if line == 'exit':
            break
        elif line == 'help':
            print('Commands:')
            print('\texit: Exit the program')
            print('\thelp: Print this help message')
            print('\t