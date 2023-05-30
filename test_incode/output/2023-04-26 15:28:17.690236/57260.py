#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that converts a list of numbers or opens user input. """    
    while True:
        try:
            number = int(input('Enter a number: '))
            break
        except ValueError:
            print('Invalid number')
            continue
    
    if number < 0:
        print('Negative number')
    else:
        print('The number is', number)
    
