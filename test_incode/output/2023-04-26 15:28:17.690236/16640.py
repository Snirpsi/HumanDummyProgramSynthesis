#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that enumerates user input and iterates over user input. """    
    while True:
        line = input('Enter a string: ')
        if line == 'quit':
            break
        else:
            print(line)
