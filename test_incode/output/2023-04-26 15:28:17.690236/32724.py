#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that stores numbers. """    
    
    while True:
        number = int(input('Enter a number: '))
        
        if number > 10:
            print('The number is too big.')
        else:
            print('The number is OK.')
            
        