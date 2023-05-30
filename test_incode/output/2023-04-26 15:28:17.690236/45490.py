#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that iterates over user input and iterates over user input. """    
    while True:
        line = input('Enter a number: ')
        if line == 'exit':
            break
        else:
            print(line)
