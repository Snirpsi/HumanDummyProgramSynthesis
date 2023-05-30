#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that converts a list of numbers or multiplyes numbers. """    
    
    while(True):
        
        number = input('Enter a number: ')
        
        if number == 'exit':
            break
        
        number = int(number)
        
        if number % 2 == 0:
            print(number, 'is a perfect square')
        else:
            print(number, 'is a square of 