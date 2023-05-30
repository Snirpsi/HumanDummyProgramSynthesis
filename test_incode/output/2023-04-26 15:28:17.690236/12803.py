#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that converts a port or multiplyes a list of numbers. """    
    
    while True:
        number = input('Enter a number: ')
        if number == 'exit':
            break
        
        try:
            number = int(number)
        except ValueError:
            print('That is not a valid number')
            continue
        
        if number % 2 == 0:
            print(number * 2)
        else:
            print(number * 