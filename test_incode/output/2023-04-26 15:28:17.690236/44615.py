#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that returns a list of numbers and converts user input. """    
    while True:
        number = int(input('Enter a number: '))
        if number == -1:
            break
        else:
            print('The number is', number)
    
