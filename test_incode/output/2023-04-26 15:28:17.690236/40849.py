#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that prints user input and converts numbers. """    
    while True:
        try:
            number = int(input('Enter a number: '))
            break
        except ValueError:
            print('Invalid number')
            
    print('You entered ', number, ', and ', number * 