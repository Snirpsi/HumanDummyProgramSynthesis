#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that returns numbers. """    
    import sys
    
    numbers = sys.stdin.readlines()
    
    for number in numbers:
        number = number.strip()
        
        if number:
            number = int(number)
            
            print(number)
            
        else:
            print('')
            
