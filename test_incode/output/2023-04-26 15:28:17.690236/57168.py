#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that prints user input and removes user input. """    
    while True:
        line = input('Enter a string: ')
        if line == '':
            break
        print('You entered:', line)
        