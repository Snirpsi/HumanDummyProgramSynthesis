#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that prints user input. """    
    while True:
        line = input('Enter a number: ')
        if line == 'done':
            print('Goodbye!')
            break
        else:
            print(line)
