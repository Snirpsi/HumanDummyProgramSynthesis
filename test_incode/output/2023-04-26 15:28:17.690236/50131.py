#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that prints user input and enumerates a list of numbers. """    
    while True:
        number = input('Enter a number: ')
        number = int(number)
        if number < 0 or number > 10:
            print('Invalid number!')
        else:
            print(number)
            
