#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that removes user input and prints a list of numbers. """    
    while True:
        number = int(input('Enter a number: '))
        print('You entered a number of', number)
        
        if number == 