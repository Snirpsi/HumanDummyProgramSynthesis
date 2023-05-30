#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that prints user input. """    
    
    # Print user input
    while True:
        try:
            line = input('Enter a number: ')
            print(line)
        except EOFError:
            print('Bye!')
            break
