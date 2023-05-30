#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that returns numbers or adds numbers. """    
    
    sum = 0
    
    while True:
        try:
            number = int(input('Enter a number: '))
            sum += number
        except ValueError:
            print('Invalid input')
            continue
        
        if number == 