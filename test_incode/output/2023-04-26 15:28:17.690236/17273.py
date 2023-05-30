#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that enumerates numbers or calculates user input. """    
    while True:
        number = int(input('Enter a number: '))
        if number < 0 or number > 1000:
            print('Invalid number')
        else:
            print('The number is', number)
            break
    
