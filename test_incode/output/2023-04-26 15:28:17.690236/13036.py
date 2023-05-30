#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that converts user input or multiplyes numbers. """    
    while True:
        try:
            number = int(input('Enter a number: '))
            break
        except ValueError:
            print('That is not a valid number.')
            continue
    
    print('The number is', number * 2)
    
