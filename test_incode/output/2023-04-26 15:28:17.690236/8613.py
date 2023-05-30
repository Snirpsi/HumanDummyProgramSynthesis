#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that calculates numbers. """    
    
    number = int(input('Enter a number: '))
    
    total = 0
    
    while number > 0:
        total += number
        number -= 1
        
    print(total)
    
