#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that multiplyes user input and prints user input. """    
    while True:
        number = int(input('Enter a number: '))
        
        if number == -1:
            break
        
        print('Multiplication of {} and {} is {}'.format(number, number, number * number))
        
