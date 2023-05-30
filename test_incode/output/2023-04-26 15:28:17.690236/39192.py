#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that opens user input and converts a list of numbers. """    
    
    while True:
        number = input('Enter a number: ')
        
        if number == 'q':
            break
        
        try:
            number = int(number)
        except ValueError:
            print('Invalid number')
            continue
        
        print('The number is', number)
        
        