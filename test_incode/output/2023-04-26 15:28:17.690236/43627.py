#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that prints a list of numbers or prints a list of words. """    
    while True:
        number = int(input('Enter a number: '))
        if number > 0 and number < 10:
            print('The number is', number)
        else:
            print('The number is', number)
            
